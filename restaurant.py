TAX_RATE = 0.05  
menu = {
    "Veg Burger": 120,
    "Cheese Burger": 150,
    "French Fries": 100,
    "Veg Pizza": 220,
    "Paneer Pizza": 280,
    "Veg Noodles": 140,
    "Hakka Noodles": 160,
    "Chilli Paneer": 220,
    "Veg Manchurian": 180,
    "Paneer Tikka": 240,
    "Masala Dosa": 120,
    "Paneer Sandwich": 140,
    "Veg Sandwich": 100,
    "Veg Biryani": 180,
    "Paneer Biryani": 220,
    "Dal Tadka": 150,
    "Paneer Butter Masala": 220,
    "Butter Naan": 50,
    "Tandoori Roti": 30,
    "Plain Rice": 100,
    "Cold Coffee": 100,
    "Lemon Soda": 70,
    "Virgin Mojito": 120,
    "Fresh Lime Juice": 80,
    "Masala Tea": 50,
    "Coffee": 70,
    "Mineral Water": 30,
}
cart = {}

def show_menu():
    print("\n------ MENU ------")
    for item, price in menu.items():
        print(f"{item:<15} - ₹{price}")

def show_cart():
    print("\n------ YOUR CART ------")
    if len(cart) == 0:
        print("Cart is empty.")
        return
    for item, qty in cart.items():
        print(f"{item:<15} x{qty}  = ₹{menu[item] * qty}")

def get_quantity():
    text = input("Enter quantity: ").strip()
    if not text.isdigit():
        print("Please enter a valid whole number!")
        return 0
    qty = int(text)
    if qty <= 0:
        print("Quantity must be at least 1.")
        return 0
    return qty

def add_item(item):
    qty = get_quantity()
    if qty > 0:
        if item in cart:
            cart[item] = cart[item] + qty
        else:
            cart[item] = qty
        print(f"{qty} x {item} added!")

def remove_item():
    if len(cart) == 0:
        print("Cart is empty, nothing to remove.")
        return
    show_cart()
    item = input("Enter item name to remove: ").strip().title()
    if item not in cart:
        print("That item is not in your cart.")
        return
    qty = get_quantity()
    if qty > 0:
        cart[item] = cart[item] - qty
        if cart[item] <= 0:
            del cart[item]  
        print("Cart updated.")

def print_bill():
    subtotal = 0
    print("\n========= BILL =========")
    for item, qty in cart.items():
        amount = menu[item] * qty
        subtotal += amount
        print(f"{item:<15} x{qty}  = ₹{amount}")
    tax = subtotal * TAX_RATE
    print("------------------------")
    print(f"Subtotal : ₹{subtotal:.2f}")
    print(f"GST (5%) : ₹{tax:.2f}")
    print(f"TOTAL    : ₹{subtotal + tax:.2f}")
    print("Thank you! Visit again.")

show_menu()
print("\nType an item name to add it.")
print("Other commands: remove, cart, menu, done")

while True:
    order = input("\nEnter item name or command: ").strip().title()

    if order == "Done":
        if len(cart) == 0:
            print("Your cart is empty. Please order something first.")
        else:
            print_bill()
            break
    elif order == "Remove":
        remove_item()
    elif order == "Cart":
        show_cart()
    elif order == "Menu":
        show_menu()
    elif order in menu:
        add_item(order)
    else:
        print("Item not found. Check the spelling.")