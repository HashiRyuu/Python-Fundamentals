from tkinter import *

# Create the main window object
# This is the base window that will hold all widgets
window = Tk()

# Set the title that appears at the top of the window
window.title("The 1927 Fifth Solvay Conference in Brussels, Belgium")

# Set the size of the window
# Format is "width x height"
window.geometry("1100x780")

# Set the background color of the main window
window.configure(background = "black")


# Adding a photo

# Load an image file
# PhotoImage works best with .gif files in basic Tkinter
photo = PhotoImage(file = "conference.gif")

# Create a Label widget to display the image
# Labels can display either text or images
image_label = Label(window, image = photo)

# Place the image label into the window
# pack() automatically positions the widget in the window
image_label.pack()


# Adding a label

# Create a label that asks the user (text)
# Background color of the label (bg)
# Text color (fg)
# Font family, size, and style (font)
name_label = Label( window, text = "Who is your favorite physicist:", 
                    bg = "black", fg = "white", 
                    font = ("Times New Roman", 16, "bold"))

# Display the label in the window
name_label.pack()



# Adding a textfield

# Create an Entry widget
# This lets the user type one line of text
# Width of the input box
# Background color of the input box (bg)
textEntry = Entry(window, width = 30, bg = "white")

# Display the text entry box
textEntry.pack()



# Adding a label and radiobutton

# Create another label asking the user
section_label = Label(window, text = "Enter your physics field interest:",
                      bg = "black", fg = "white", 
                      font = ("Times New Roman", 16, "bold"))

# Display the label
section_label.pack()

# IntVar stores the value selected by the radio buttons
# If the user selects Quantum Physics, sections_var becomes 1
# If the user selects Classical Physics, sections_var becomes 2
# Connect this radio button to sections_var (variable)
# Store number when this button is selected (value)
sections_var = IntVar()
radio1 = Radiobutton(window, text = "Quantum Physics", variable = sections_var,
                     value = 1)
radio2 = Radiobutton(window, text = "Classical Physics", variable = sections_var,
                     value = 2)

# Display the radio buttons
radio1.pack()
radio2.pack()


# This function runs when the user clicks the Submit button
def click():
    
    # Get the text that the user typed into the Entry box
    name = textEntry.get()
    
    # Print the favorite physicist into the output Text box
    output.insert(END, "Your favorite physicist is " + name + "\n")
    
    # Check which radio button was selected
    # sections_var.get() returns the selected radio button value    
    if sections_var.get() == 1:
        msg = "\nYour physics field interest is Quantum Physics"
        
    elif sections_var.get() == 2:
        msg = "\nYour physics field interest is Classical Physics"
        
    else:
        msg = "\nYou did not select a physics field interest."    
    
    # Insert the final message into the output Text box   
    output.insert(END, msg + "\n\n")
    


#adding a button

# Create a button
# command=click means the click() function runs when the button is pressed
submit_button =  Button(window, text = "Submit", width = 20, command = click)
submit_button.pack()


#adding a text area

# Create a Text widget
# This is a larger box that can display multiple lines of text
# Wrap text by words instead of cutting words in half (warp)
output = Text(window, width = 50, height = 50, wrap = WORD, background = "white")
output.pack()


# Start the Tkinter event loop
# This keeps the window open and waits for user actions
window.mainloop()
