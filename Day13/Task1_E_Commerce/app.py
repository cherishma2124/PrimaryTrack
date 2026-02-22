from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, Field, ValidationError
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


class ItemCreate(BaseModel):
    name: str = Field(min_length=2)
    category: str = Field(min_length=2)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    
class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2)
    category: Optional[str] = Field(default=None, min_length=2)
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

class RegisterSchema(BaseModel):
    fullname: str = Field(min_length=2)
    email: str = Field(min_length=5)
    password: str = Field(min_length=4)

class LoginSchema(BaseModel):
    email: str = Field(min_length=5)
    password: str = Field(min_length=4)

def get_cart():
    if "cart" not in session:
        session["cart"] = {}
    return session["cart"]

def is_logged_in():
    return "user_id" in session

def login_required():
    if not is_logged_in():
        flash("Please login first!", "danger")
        return False
    return True

def cart_total(cart):
    total = 0
    for item_id, qty in cart.items():
        item = Item.query.get(int(item_id))
        if item:
            total += item.price * qty
    return total


@app.route("/")
def home():
    category = request.args.get("category")
    q = request.args.get("q")

    query = Item.query
    if category:
        query = query.filter(Item.category.ilike(f"%{category}%"))
    if q:
        query = query.filter(Item.name.ilike(f"%{q}%"))

    items = query.all()
    return render_template("home.html", items=items)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = {
            "fullname": request.form.get("fullname"),
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }

        try:
            validated = RegisterSchema(**data)
        except ValidationError as e:
            flash("Invalid input!", "danger")
            return redirect(url_for("register"))

        existing = User.query.filter_by(email=validated.email).first()
        if existing:
            flash("Email already exists!", "danger")
            return redirect(url_for("register"))

        user = User(
            fullname=validated.fullname,
            email=validated.email,
            password_hash=generate_password_hash(validated.password)
        )
        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = {
            "email": request.form.get("email"),
            "password": request.form.get("password"),
        }

        try:
            validated = LoginSchema(**data)
        except ValidationError:
            flash("Invalid input!", "danger")
            return redirect(url_for("login"))

        user = User.query.filter_by(email=validated.email).first()
        if not user or not check_password_hash(user.password_hash, validated.password):
            flash("Invalid email or password!", "danger")
            return redirect(url_for("login"))

        session["user_id"] = user.id
        session["user_name"] = user.fullname
        session.modified = True

        flash("Login successful!", "success")
        return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "warning")
    return redirect(url_for("home"))

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        name = request.form.get("name")
        category = request.form.get("category")
        price = request.form.get("price")
        stock = request.form.get("stock")

        if not name or not category or not price or not stock:
            flash("All fields are required!", "danger")
            return redirect(url_for("upload"))

        try:
            item = Item(
                name=name,
                category=category,
                price=float(price),
                stock=int(stock)
            )
            db.session.add(item)
            db.session.commit()
            flash("Item added successfully!", "success")
            return redirect(url_for("results"))
        except:
            flash("Invalid input values!", "danger")

    return render_template("upload.html")

@app.route("/results")
def results():
    items = Item.query.all()
    return render_template("results.html", items=items)


@app.route("/cart")
def view_cart():
    if not login_required():
        return redirect(url_for("login"))

    cart = get_cart()
    cart_items = []

    for item_id, qty in cart.items():
        item = Item.query.get(int(item_id))
        if item:
            cart_items.append({
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "qty": qty,
                "subtotal": item.price * qty
            }) 

    total = cart_total(cart)
    return render_template("cart.html", cart_items=cart_items, total=total)

@app.route("/cart/add/<int:item_id>")
def add_cart(item_id):
    cart = get_cart()

    item = Item.query.get(item_id)
    if not item:
        flash("Item not found!", "danger")
        return redirect(url_for("home"))

    if item.stock <= 0:
        flash("Out of stock!", "danger")
        return redirect(url_for("home"))

    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    session["cart"] = cart
    flash("Added to cart!", "success")
    return redirect(url_for("home"))


@app.route("/cart/remove/<int:item_id>")
def remove_cart(item_id):
    cart = get_cart()
    cart.pop(str(item_id), None)
    session["cart"] = cart
    flash("Removed from cart!", "warning")
    return redirect(url_for("view_cart"))

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if not login_required():
        return redirect(url_for("login"))

    cart = get_cart()
    if not cart:
        flash("Cart is empty!", "danger")
        return redirect(url_for("home"))

    total = cart_total(cart)

    if request.method == "POST":
        return redirect(url_for("payment"))

    return render_template("checkout.html", total=total)

@app.route("/payment", methods=["GET", "POST"])
def payment():
    if not login_required():
        return redirect(url_for("login"))

    cart = get_cart()
    if not cart:
        flash("Cart is empty!", "danger")
        return redirect(url_for("home"))

    total = cart_total(cart)

    if request.method == "POST":
        card = request.form.get("card")
        name = request.form.get("name")

        if not card or not name:
            flash("All fields required!", "danger")
            return redirect(url_for("payment"))

    
        if card.strip().endswith("0"):
            return render_template("payment_failed.html", total=total)

        for item_id, qty in cart.items():
            item = Item.query.get(int(item_id))
            if item:
                item.stock -= qty

        db.session.commit()

        session["cart"] = {}

        return render_template("payment_success.html", total=total)

    return render_template("payment.html", total=total)

@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    return jsonify([
        {"id": i.id, "name": i.name, "category": i.category, "price": i.price, "stock": i.stock}
        for i in items
    ])

@app.route("/items", methods=["POST"])
def create_item():
    try:
        validated = ItemCreate(**(request.json or {}))
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    item = Item(**validated.model_dump())
    db.session.add(item)
    db.session.commit()
    return jsonify({"message": "Item created", "id": item.id}), 201

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    try:
        validated = ItemUpdate(**(request.json or {}))
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    data = validated.model_dump(exclude_none=True)
    for key, value in data.items():
        setattr(item, key, value)

    db.session.commit()
    return jsonify({"message": "Item updated"}), 200

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted"}), 200

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)