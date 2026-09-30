# Restaurant Billing System

A simple Python command-line application for taking restaurant orders and generating an itemised bill with 5% GST.

## Author

| | |
|---|---|
| **Name** | Akshat Farkiya |
| **Reg. No.** | 26MIM10154 |
| **Branch** | Integrated M.Tech in Artificial Intelligence |
| **University** | VIT Bhopal University |

## Features

- Menu of 27 vegetarian items with prices in ₹
- Add items to a cart with quantity
- Remove items or reduce their quantity
- View the cart and menu at any time
- Input validation (only whole numbers of 1 or more)
- Case-insensitive item names (`veg burger` works)
- Final bill with subtotal, 5% GST and grand total
- Uses only standard Python, no extra libraries

## Requirements

- Python 3.x

## How to Run

```bash
python restaurant_billing.py
```

## Commands

| Command | What it does |
|---|---|
| Item name (e.g. `Veg Burger`) | Asks for quantity and adds the item to the cart |
| `remove` | Shows the cart and removes or reduces an item |
| `cart` | Displays the current cart |
| `menu` | Displays the menu |
| `done` | Prints the final bill and exits |

## Sample Output

```text
------ YOUR CART ------
Veg Burger x2 = ₹240
Cold Coffee x1 = ₹100

========= BILL =========
Veg Burger x2 = ₹240
Cold Coffee x1 = ₹100
------------------------
Subtotal : ₹340.00
GST (5%) : ₹17.00
TOTAL    : ₹357.00

Thank you! Visit again.
```

## Project Structure

```text
.
├── restaurant_billing.py                          # main program
├── README.md                                      # this file
└── Restaurant_Billing_System_Project_Report.docx
```

## How It Works

- `menu` is a dictionary mapping item names to prices.
- `cart` is a dictionary mapping item names to quantities.
- Functions: `show_menu()`, `show_cart()`, `get_quantity()`, `add_item()`, `remove_item()`, `print_bill()`.
- A `while` loop reads commands until the user types `done`.

## Future Improvements

- Graphical interface (Tkinter or web)
- Save orders and menu in a database (SQLite)
- Export bills as PDF
- Admin panel to edit the menu
- Discounts and multiple payment methods
- Partial-name search
