from flask import Flask, render_template, request, redirect, url_for, flash
from inventory import Inventory
from storage import Storage
from models import Electronics, Grocery
from logger_decorator import log_action

app = Flask(__name__)
app.secret_key = "supersecretkey"

inventory = Inventory()
storage = Storage()


inventory.load_from_list(storage.load())
 
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def view_products():
    products = list(inventory)
    return render_template("view_products.html", products=products)


@app.route("/add", methods=["GET", "POST"])
@log_action
def add_product():
    if request.method == "POST":
        try:
            ptype = request.form.get("ptype")
            pid = request.form.get("pid").strip()
            name = request.form.get("name").strip()
            price = float(request.form.get("price"))
            stock = int(request.form.get("stock"))

            if ptype == "Electronics":
                brand = request.form.get("brand").strip()
                warranty = int(request.form.get("warranty"))
                product = Electronics(pid, name, price, stock, brand, warranty)

            elif ptype == "Grocery":
                expiry = request.form.get("expiry").strip()
                product = Grocery(pid, name, price, stock, expiry)

            else:
                flash("Invalid product type!", "danger")
                return redirect(url_for("add_product"))

            inventory.add_product(product)
            storage.save(inventory)

            flash("Product added successfully!", "success")
            return redirect(url_for("view_products"))

        except Exception as e:
            flash(str(e), "danger")
            return redirect(url_for("add_product"))

    return render_template("add_product.html")


@app.route("/delete/<pid>")
@log_action
def delete_product(pid):
    try:
        inventory.remove_product(pid)
        storage.save(inventory)
        flash("Product deleted successfully!", "warning")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("view_products"))


@app.route("/update_stock/<pid>", methods=["POST"])
@log_action
def update_stock(pid):
    try:
        mode = request.form.get("mode")
        qty = int(request.form.get("qty"))

        inventory.update_stock(pid, qty, mode)
        storage.save(inventory)

        flash("Stock updated successfully!", "success")
    except Exception as e:
        flash(str(e), "danger")

    return redirect(url_for("view_products"))


@app.route("/search", methods=["GET", "POST"])
def search():
    results = []
    if request.method == "POST":
        keyword = request.form.get("keyword")
        results = inventory.search(keyword)

    return render_template("search.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)