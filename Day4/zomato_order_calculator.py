menu = {
    1: ("Burger", 120),
    2: ("Pizza", 250),
    3: ("Biryani", 180),
    4: ("Pasta", 150)
}
cart = {}
try:
    print("------ ZOMATO MENU ------")
    for key, value in menu.items():
        print(f"{key}. {value[0]} - Rs{value[1]}")

    while True:
        choice = int(input("\nEnter item number (0 to finish): "))

        if choice == 0:
            break

        if choice not in menu:
            print(" Invalid item number")
            continue

        qty = int(input("Enter quantity: "))

        if qty <= 0:
            print(" Quantity must be greater than zero")
            continue

        cart[choice] = cart.get(choice, 0) + qty

    if not cart:
        raise Exception("No items selected")

    print("\n------ BILL DETAILS ------")
    subtotal = 0

    for item_id, qty in cart.items():
        name, price = menu[item_id]
        cost = price * qty
        subtotal += cost
        print(f"{name} x {qty} = Rs{cost}")

    gst = subtotal * 0.05
    delivery_charge = 40
    total = subtotal + gst + delivery_charge

    print("-------------------------")
    print(f"Subtotal        : Rs{subtotal}")
    print(f"GST (5%)        : Rs{gst:.2f}")
    print(f"Delivery Charge : Rs{delivery_charge}")
    print(f"Total Amount    : Rs{total:.2f}")
except ValueError:
    print(" Please enter numbers only")
except Exception as e:
    print(" Error:", e)
finally:
    print("\nThank you for ordering with Zomato")