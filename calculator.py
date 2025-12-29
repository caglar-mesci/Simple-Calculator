"""
Simple Calculator Application
--------------------------------
This is a basic calculator built using Python's tkinter library.
It supports addition, subtraction, multiplication, and division.

Date: 21.12.2025
"""

# Import everything from tkinter for GUI components
from tkinter import *

# -----------------------------
# Main Window Configuration
# -----------------------------
window = Tk()
window.title("Simple Calculator")           # Title of the window
window.geometry("270x250+300+100")           # Window size and position
window.resizable(0, 0)                       # Disable resizing

# -----------------------------
# Global Variable
# -----------------------------
store = ""                                   # Stores the mathematical expression


# -----------------------------
# Calculator Logic
# -----------------------------
def calculate(key):
    """
    Handles all button click events.
    Updates the display and evaluates expressions.
    """
    global store

    # If a number is pressed, add it to the screen and expression
    if key in "0123456789":
        screen.insert(END, key)
        store += key

    # If an operator is pressed, add it to the screen and expression
    elif key in "+-/*":
        screen.insert(END, key)
        store += key

    # If equal button is pressed, evaluate the expression
    elif key == "=":
        try:
            # Clear the screen before displaying result
            screen.delete(0, END)

            # Safely evaluate expression (no built-in functions allowed)
            result = eval(store, {"__builtins__": None}, {})

            # Display result and update stored expression
            screen.insert(0, str(result))
            store = str(result)

        except:
            # Handle invalid expressions
            screen.delete(0, END)
            screen.insert(0, "Error")
            store = ""

    # Clear the screen and reset expression
    elif key == "C":
        screen.delete(0, END)
        store = ""


# -----------------------------
# Display (Entry Widget)
# -----------------------------
screen = Entry(width=40, justify=RIGHT)      # Calculator display
screen.grid(row=0, column=0, columnspan=3, ipady=10)


# -----------------------------
# Buttons Configuration
# -----------------------------
list_buttons = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
    "+", "0", "-",
    "*", "/", 
    "C", "="
]

row = 1
col = 0

# Create and place buttons dynamically
for i in list_buttons:
    command = lambda x=i: calculate(x)

    Button(
        text=i,
        font="verdana 8 bold",
        width=10,
        height=2,
        relief=GROOVE,
        command=command
    ).grid(row=row, column=col)

    col += 1
    if col > 2:
        col = 0
        row += 1


# -----------------------------
# Run Application
# -----------------------------
window.mainloop()

