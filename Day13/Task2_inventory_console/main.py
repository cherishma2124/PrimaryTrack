from models import Electronics, Grocery
from inventory import Inventory
from storage import Storage
from logger_decorator import log_action
import ui


inventory = Inventory()
storage = Storage()


inventory.load_from_list(storage.load())


@log_action
def add_product():
    ui.header("ADD PRODUCT")
    ptype = input("Type (1=Electronics, 2=Grocery): ").strip()

    pid = input("Product ID: ").strip()
    name = input("Name: ").strip()
    price = ui.input_float("Price: ")
    stock = ui.input_int("Stock: ")

    if ptype == "1":
        brand = input("Brand: ").strip()
        warranty = ui.input_int("Warranty years: ")
        product = Electronics(pid, name, price, stock, brand, warranty)

    elif ptype == "2":
        expiry = input("Expiry date (YYYY-MM-DD): ").strip()
        product = Grocery(pid, name, price, stock, expiry)

    else:
        print("Invalid product type!")
        return

    inventory.add_product(product)
    print("Product added successfully!")


@log_action
def remove_product():
    ui.header("REMOVE PRODUCT")
    pid = input("Enter Product ID: ").strip()
    inventory.remove_product(pid)
    print("Product removed successfully!")


@log_action
def update_stock():
    ui.header("UPDATE STOCK")
    pid = input("Enter Product ID: ").strip()
    mode = input("Mode (add/remove): ").strip().lower()
    qty = ui.input_int("Quantity: ")

    inventory.update_stock(pid, qty, mode)
    print("Stock updated!")


@log_action
def search_product():
    ui.header("SEARCH PRODUCT")
    keyword = input("Enter name or ID keyword: ").strip()
    results = inventory.search(keyword)

    if not results:
        print("No products found!")
        return

    print("\n--- Results ---")
    for p in results:
        print(p)


@log_action
def view_all():
    ui.header("ALL PRODUCTS")
    found = False
    for p in inventory:   
        found = True
        print(p)

    if not found:
        print("Cart is empty (No products in inventory).")


@log_action
def save_inventory():
    storage.save(inventory)
    print("Inventory saved to file!")


def main():
    while True:
        ui.header("INVENTORY MANAGEMENT SYSTEM (OOP)")
        ui.menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                add_product()
            elif choice == "2":
                remove_product()
            elif choice == "3":
                update_stock()
            elif choice == "4":
                search_product()
            elif choice == "5":
                view_all()
            elif choice == "6":
                save_inventory()
            elif choice == "7":
                save_inventory()
                print("Exiting... Inventory saved!")
                break
            else:
                print(" Invalid choice!")

        except Exception as e:
            print(f" Error: {e}")


if __name__ == "__main__":
    main()