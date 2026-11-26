# Description:
# This program creates a pizza ordering GUI using Tkinter.
# The user chooses a pizza size, crust type, and toppings.
# When the Submit Order button is clicked, the program calculates
# the subtotal, tax, and final total, then displays a receipt.

import tkinter as tk


# Constants
# -----------------------------

SMALL_PRICE = 10.99
MEDIUM_PRICE = 12.99
LARGE_PRICE = 14.99

TOPPING_PRICE = 1.25
TAX_RATE = 0.0875


# -----------------------------
# Main window setup
# -----------------------------

window = tk.Tk()
window.title("Mice and Adam's Pizza")
window.geometry("850x720")
window.resizable(False, False)


# -----------------------------
# Image section
# -----------------------------
# The image file must be saved in the same folder as this Python file.
# Tkinter works very well with GIF images through PhotoImage.

menu_image = tk.PhotoImage(file="pizza_menu.gif")
image_label = tk.Label(window, image=menu_image)
image_label.pack(pady=10)


# -----------------------------
# Variables connected to widgets
# -----------------------------
# StringVar stores the selected radio button value.
# IntVar stores whether each checkbox is checked.
# A value of 1 means checked, and a value of 0 means not checked.

customer_name = tk.StringVar()

size_var = tk.StringVar()
size_var.set("small")       # default pizza size

crust_var = tk.StringVar()
crust_var.set("Hand-tossed")  # default crust

pepperoni_var = tk.IntVar()
sausage_var = tk.IntVar()
mushroom_var = tk.IntVar()
onion_var = tk.IntVar()


# -----------------------------
# click() function
# -----------------------------
# This function runs when the user clicks the Submit Order button.
# It reads the user's selections, calculates the cost, and updates
# the receipt display.

def click():
    # Get selected pizza size.
    selected_size = size_var.get()

    # Use if/elif/else control flow to choose the base pizza price.
    if selected_size == "small":
        size_text = "small pizza"
        base_price = SMALL_PRICE
    elif selected_size == "medium":
        size_text = "medium pizza"
        base_price = MEDIUM_PRICE
    else:
        size_text = "large pizza"
        base_price = LARGE_PRICE

    # Get selected crust type.
    crust_text = crust_var.get()

    # Cheese is the default topping.
    toppings = ["Cheese"]

    # Count additional toppings.
    extra_topping_count = 0

    if pepperoni_var.get() == 1:
        toppings.append("Pepperoni")
        extra_topping_count += 1

    if sausage_var.get() == 1:
        toppings.append("Sausage")
        extra_topping_count += 1

    if mushroom_var.get() == 1:
        toppings.append("Mushroom")
        extra_topping_count += 1

    if onion_var.get() == 1:
        toppings.append("Onion")
        extra_topping_count += 1

    # Calculate subtotal, tax, and final total.
    toppings_cost = extra_topping_count * TOPPING_PRICE
    subtotal = base_price + toppings_cost
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Convert the toppings list into one readable string.
    toppings_text = " ".join(toppings)

    # Build the receipt text.
    receipt = ""
    receipt += "Your Receipt...\n"

    # The optional customer name is included in the receipt.
    if customer_name.get() != "":
        receipt += "Customer: " + customer_name.get() + "\n"

    receipt += "Your order: " + size_text + "\n"
    receipt += "Crust type: " + crust_text + "\n"
    receipt += "Toppings: " + toppings_text + "\n"
    receipt += "Tax: $" + format(tax, ".2f") + "\n"
    receipt += "Your final cost is: $" + format(total, ".2f")

    # Update the receipt label on the GUI.
    receipt_label.config(text=receipt)


# -----------------------------
# Form section
# -----------------------------

form_frame = tk.Frame(window)
form_frame.pack(pady=5)

name_label = tk.Label(form_frame, text="Enter your name:")
name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

name_entry = tk.Entry(form_frame, textvariable=customer_name, width=25)
name_entry.grid(row=0, column=1, sticky="w", padx=10, pady=5)


# -----------------------------
# Pizza size radio buttons
# -----------------------------

size_frame = tk.LabelFrame(window, text="Choose a pizza size")
size_frame.pack(fill="x", padx=30, pady=8)

small_button = tk.Radiobutton(
    size_frame,
    text="Small $10.99",
    variable=size_var,
    value="small"
)
small_button.pack(side="left", padx=30, pady=8)

medium_button = tk.Radiobutton(
    size_frame,
    text="Medium $12.99",
    variable=size_var,
    value="medium"
)
medium_button.pack(side="left", padx=30, pady=8)

large_button = tk.Radiobutton(
    size_frame,
    text="Large $14.99",
    variable=size_var,
    value="large"
)
large_button.pack(side="left", padx=30, pady=8)


# -----------------------------
# Crust type radio buttons
# -----------------------------

crust_frame = tk.LabelFrame(window, text="Choose a crust type")
crust_frame.pack(fill="x", padx=30, pady=8)

hand_button = tk.Radiobutton(
    crust_frame,
    text="Hand-tossed",
    variable=crust_var,
    value="Hand-tossed"
)
hand_button.pack(side="left", padx=30, pady=8)

deep_button = tk.Radiobutton(
    crust_frame,
    text="Deep-dish",
    variable=crust_var,
    value="Deep-dish"
)
deep_button.pack(side="left", padx=30, pady=8)

thin_button = tk.Radiobutton(
    crust_frame,
    text="Thin-crust",
    variable=crust_var,
    value="Thin-crust"
)
thin_button.pack(side="left", padx=30, pady=8)


# -----------------------------
# Toppings checkboxes
# -----------------------------

topping_frame = tk.LabelFrame(window, text="Choose toppings")
topping_frame.pack(fill="x", padx=30, pady=8)

cheese_label = tk.Label(topping_frame, text="Cheese is included by default.")
cheese_label.pack(anchor="w", padx=20, pady=3)

pepperoni_check = tk.Checkbutton(
    topping_frame,
    text="Pepperoni",
    variable=pepperoni_var
)
pepperoni_check.pack(side="left", padx=25, pady=8)

sausage_check = tk.Checkbutton(
    topping_frame,
    text="Sausage",
    variable=sausage_var
)
sausage_check.pack(side="left", padx=25, pady=8)

mushroom_check = tk.Checkbutton(
    topping_frame,
    text="Mushroom",
    variable=mushroom_var
)
mushroom_check.pack(side="left", padx=25, pady=8)

onion_check = tk.Checkbutton(
    topping_frame,
    text="Onion",
    variable=onion_var
)
onion_check.pack(side="left", padx=25, pady=8)


# -----------------------------
# Submit button
# -----------------------------

submit_button = tk.Button(
    window,
    text="Submit Order",
    command=click,
    width=20
)
submit_button.pack(pady=12)


# -----------------------------
# Receipt output
# -----------------------------

receipt_frame = tk.LabelFrame(window, text="Receipt")
receipt_frame.pack(fill="both", expand=True, padx=30, pady=10)

receipt_label = tk.Label(
    receipt_frame,
    text="Your receipt will appear here after you submit your order.",
    justify="left",
    anchor="nw",
    font=("Courier New", 12),
    bg="white",
    width=70,
    height=8
)
receipt_label.pack(fill="both", expand=True, padx=10, pady=10)


# -----------------------------
# Start the GUI event loop
# -----------------------------

window.mainloop()
