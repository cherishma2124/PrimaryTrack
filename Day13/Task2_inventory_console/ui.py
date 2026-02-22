def header(title):
    print("\n" + "=" * 60)
    print(f"{title.center(60)}")
    print("=" * 60)


def menu():
    print("""
1. Add Product
2. Remove Product
3. Update Stock
4. Search Product
5. View All Products
6. Save Inventory
7. Exit
""")


def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Enter a valid number!")


def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Enter a valid price!")