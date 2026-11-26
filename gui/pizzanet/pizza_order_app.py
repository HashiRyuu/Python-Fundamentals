# Program: PizzaNet Pizza Ordering Application
#
# Description:
# This program creates a pizza ordering GUI using Tkinter.
# The user can choose a pizza size, crust type, and toppings.
# The program calculates the subtotal, tax, and final total.
# When the user clicks the Submit Order button, a receipt is
# displayed on the screen with the full order information.

from tkinter import *

# -----------------------------
# Constants
# -----------------------------
# These constants store the fixed prices used in the program.
# Pizza sizes have fixed base prices.
# Each extra topping costs $1.25.
# The tax rate is 8.75%.
SMALL_PRICE = 10.99
MEDIUM_PRICE = 12.99
LARGE_PRICE = 14.99

TOPPING_PRICE = 1.25
TAX_RATE = 0.0875


# -----------------------------
# Main window setup
# -----------------------------
# This section creates the main Tkinter window.
# It sets the window title, size, and background color.
window = Tk()
window.title("PizzaNet")
window.geometry("1500x1000")
window.configure(background = "White")


# -----------------------------
# Header text
# -----------------------------
# This label displays the title of the pizza ordering program
# at the top of the GUI.
Header_label = Label(
    window,
    text="Welcome to PizzaNet",
    bg="Black",
    fg="White",
    font=("Courier New", 30, "bold")
)

Header_label.place(x=520, y=0)


# -----------------------------
# Build your own
# -----------------------------
# This section display text
Build_label = Label(
    window,
    text="Build your own pizza",
    bg="White",
    fg="Black",
    font=("Courier New", 30, "bold")
)

Build_label.place(x=10, y=110)


# -----------------------------
# Pizza Image section
# -----------------------------
# This section loads the pizza menu image and displays it on the GUI.
# The image file must be in the same folder as this Python file.
menu_image = PhotoImage(file="pizza_menu.gif")

menu_label = Label(window, image=menu_image, bg="White")
menu_label.place(x=600, y=130)


# -----------------------------
# Variables connected to widgets
# -----------------------------
# StringVar stores text-based user choices, such as size and crust type.
# IntVar stores checkbox values.
# A checkbox value of 1 means selected, and 0 means not selected.
# The subtotal, tax, total, and checkout message variables update labels on the GUI.
customer_name = StringVar()

size_var = StringVar()
size_var.set("small")       # default pizza size

crust_var = StringVar()
crust_var.set("Hand-tossed")  # default crust

pepperoni_var = IntVar()
sausage_var = IntVar()
mushroom_var = IntVar()
onion_var = IntVar()

subtotal_var = StringVar()
subtotal_var.set("Subtotal: $0.00")

tax_var = StringVar()
tax_var.set("Tax: $0.00")

total_var = StringVar()
total_var.set("Total: $0.00")

checkout_message_var = StringVar()
checkout_message_var.set("")


# -----------------------------
# click() function
# -----------------------------
# This function runs when the user clicks the Submit Order button.
# It reads the selected pizza size, crust type, and toppings.
# It then calculates the subtotal, tax, and total cost.
# Finally, it updates the order summary labels and displays the receipt.
subtotal = 0
tax = 0
total = 0
def click():
    # Get the selected pizza size from the radio buttons.
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

    # Cheese is included by default.
    # Extra toppings are added only if their checkboxes are selected.
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

    # Calculate the topping cost, subtotal, tax, and final total.
    toppings_cost = extra_topping_count * TOPPING_PRICE
    subtotal = base_price + toppings_cost
    tax = subtotal * TAX_RATE
    total = subtotal + tax
    
    # Update the order summary labels under the Submit Order button.
    subtotal_var.set("Subtotal: $" + format(subtotal, ".2f"))
    tax_var.set("Tax: $" + format(tax, ".2f"))
    total_var.set("Total: $" + format(total, ".2f"))
    checkout_message_var.set("")    

    # Convert the toppings list into one readable string.
    toppings_text = " ".join(toppings)

    # Build the receipt text.
    receipt = ""
    receipt += "Your Receipt...\n"

    # Build the receipt text that will be displayed in the receipt box.
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
# This section creates the customer name input area.
# The Entry widget allows the user to type their name.
form_frame = Frame(window, bg="White")
form_frame.place(x=50, y=630, width=600, height=60)

name_label = Label(
    form_frame,
    text="Enter your name:",
    bg="White",
    fg="Black",
    font=("Courier New", 16, "bold")
)

name_label.place(x=0, y=10)

name_entry = Entry(
    form_frame,
    textvariable=customer_name,
    width=15,
    font=("Courier New", 16, "bold"),
    bg="White",
    fg="Black",
    insertbackground="Black",
    relief="solid",
    borderwidth=1,
    highlightthickness=1
)
name_entry.place(x=210, y=8, height=32)


# -----------------------------
# Pizza size radio buttons
# -----------------------------
# This section lets the user choose one pizza size.
# Radio buttons are used because only one size should be selected at a time.
size_frame = LabelFrame(window, text="Choose a pizza size", bg="White", 
                        font=("Courier New", 16, "bold"))
size_frame.place(x=50, y=180, width=300, height=200)

small_button = Radiobutton(
    size_frame,
    text="Small: $10.99",
    variable=size_var,
    value="small",
    bg="White",
    font=("Courier New", 20, "bold")
)
small_button.place(x=10, y=25)

medium_button = Radiobutton(
    size_frame,
    text="Medium: $12.99",
    variable=size_var,
    value="medium",
    bg="White",
    font=("Courier New", 20, "bold")
)
medium_button.place(x=10, y=70)

large_button = Radiobutton(
    size_frame,
    text="Large: $14.99",
    variable=size_var,
    value="large",
    bg="White",
    font=("Courier New", 20, "bold")
)
large_button.place(x=10, y=120)


# -----------------------------
# Crust type radio buttons
# -----------------------------
# This section lets the user choose one crust type.
# Radio buttons are used because only one crust type should be selected.
crust_frame = LabelFrame(window, text="Choose a crust type", bg="White", 
                         font=("Courier New", 16, "bold"))
crust_frame.place(x=50, y=400, width=300, height=200)

hand_button = Radiobutton(
    crust_frame,
    text="Hand-tossed",
    variable=crust_var,
    value="Hand-tossed",
    bg="White",
    font=("Courier New", 20, "bold")
)
hand_button.place(x=10, y=25)

deep_button = Radiobutton(
    crust_frame,
    text="Deep-dish",
    variable=crust_var,
    value="Deep-dish",
    bg="White",
    font=("Courier New", 20, "bold")
)
deep_button.place(x=10, y=70)

thin_button = Radiobutton(
    crust_frame,
    text="Thin-crust",
    variable=crust_var,
    value="Thin-crust",
    bg="White",
    font=("Courier New", 20, "bold")
)
thin_button.place(x=10, y=120)


# -----------------------------
# Toppings checkboxes
# -----------------------------
# This section lets the user choose additional toppings.
# Checkboxes are used because the user can choose more than one topping.
# Cheese is included by default and does not add extra cost.
topping_frame = LabelFrame(window, text="Choose toppings", bg="White", 
                           font=("Courier New", 16, "bold"))
topping_frame.place(x=600, y=485, width=800, height=120)

cheese_label = Label(
    topping_frame,
    text="Cheese is included by default.",
    bg="White",
    font=("Courier New", 16, "bold")
)
cheese_label.place(x=20, y=10)

pepperoni_check = Checkbutton(
    topping_frame,
    text="Pepperoni",
    variable=pepperoni_var,
    bg="White",
    font=("Courier New", 16, "bold")
)
pepperoni_check.place(x=20, y=45)

sausage_check = Checkbutton(
    topping_frame,
    text="Sausage",
    variable=sausage_var,
    bg="White",
    font=("Courier New", 16, "bold")
)
sausage_check.place(x=200, y=45)

mushroom_check = Checkbutton(
    topping_frame,
    text="Mushroom",
    variable=mushroom_var,
    bg="White",
    font=("Courier New", 16, "bold")
)
mushroom_check.place(x=370, y=45)

onion_check = Checkbutton(
    topping_frame,
    text="Onion",
    variable=onion_var,
    bg="White",
    font=("Courier New", 16, "bold")
)
onion_check.place(x=570, y=45)


# -----------------------------
# Submit button
# -----------------------------
# This button calls the click() function.
# It updates the receipt and order summary based on the current selections.
submit_button = Button(
    window,
    text="Submit Order",
    command=click,
    width=20
)
submit_button.place(x=50, y=680)

# -----------------------------
# checkout() function
# -----------------------------
# This function calls click() to make sure the latest order is calculated.
# It then displays a checkout confirmation message.
def checkout():
    click()
    checkout_message_var.set("Checkout complete. Thank you!")
    
    
# -----------------------------
# Order Summary section
# -----------------------------
# This section displays the subtotal, tax, and total cost separately.
# These labels update when the user clicks Submit Order.
summary_frame = LabelFrame(
    window,
    text="Order Summary",
    bg="White",
    font=("Courier New", 14, "bold")
)
summary_frame.place(x=50, y=730, width=390, height=220)

subtotal_label = Label(
    summary_frame,
    textvariable=subtotal_var,
    bg="White",
    fg="Black",
    font=("Courier New", 14, "bold")
)
subtotal_label.place(x=20, y=20)

tax_label = Label(
    summary_frame,
    textvariable=tax_var,
    bg="White",
    fg="Black",
    font=("Courier New", 14, "bold")
)
tax_label.place(x=20, y=55)

total_label = Label(
    summary_frame,
    textvariable=total_var,
    bg="White",
    fg="Black",
    font=("Courier New", 16, "bold")
)
total_label.place(x=20, y=90)

checkout_button = Button(
    summary_frame,
    text="Checkout",
    command=checkout,
    width=18,
    font=("Courier New", 10, "bold")
)
checkout_button.place(x=20, y=130)

checkout_message_label = Label(
    summary_frame,
    textvariable=checkout_message_var,
    bg="White",
    fg="Green",
    font=("Courier New", 10, "bold")
)
checkout_message_label.place(x=20, y=165)


# -----------------------------
# Receipt output
# -----------------------------
# This section displays the final receipt.
# The receipt includes the customer name, pizza size, crust type,
# toppings, subtotal, tax, and final cost.
receipt_frame = LabelFrame(window, text="Receipt", bg="White", 
                           font=("Courier New", 16, "bold"))
receipt_frame.place(x=600, y=640, width=800, height=280)

receipt_label = Label(
    receipt_frame,
    text="Your receipt will appear here after you submit your order.",
    justify="left",
    anchor="nw",
    font=("Courier New", 16, "bold"),
    bg="white",
    width=70,
    height=8
)
receipt_label.place(x=10, y=10, width=670, height=160)


# -----------------------------
# Start the GUI event loop
# -----------------------------
# mainloop() keeps the GUI window open and waits for user actions,
# such as button clicks and checkbox selections.
window.mainloop()
