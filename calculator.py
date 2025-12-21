
## Hello, I built this simple calculator using tkinter in Python.
## It can calculate basic calclations like addition, subtraction, multiplication, and division.
## I hope you enjoy using it!

## 21.12.2025 - 04.43


#we import everything from tkinter
from tkinter import *

window = Tk()
window.title("Simple Calculator")   #name of our calculator
window.geometry("270x250+300+100")  #sizes and position
window.resizable(0, 0)              #resizing disabled


store = ""                          #to store the input expression


def calculate(key):                 #lets start the function
    
    global store

    if key in "0123456789":         #numbers shown on screen
        screen.insert(END, key)
        store += key


    elif key in "+-/*":             #operators shown on screen
        screen.insert(END, key)   
        store += key



    #equal
    elif key == "=":
        try:
            # Disable built-in functions to restrict eval to safe mathematical expressions only
            screen.delete(0, END)
            result = eval(store, {"__builtins__": None}, {})     
            screen.insert(0, str(result))   
            store = str(result)

        except:
            screen.delete(0, END)
            screen.insert(0, "Error")
            store = ""


    # clear
    elif key == "C":
        screen.delete(0, END)
        store = ""


# Entry widget used as the calculator display (aligned to the right)
screen = Entry(width=40, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=3, ipady=10)


#button lineup
list_buttons = ["1", "2", "3",
                "4", "5", "6",
                "7", "8", "9",
                "+", "0","-",
                "*",      "/",
                "C",      "="]

row = 1
col = 0

for i in list_buttons:

    command = lambda x=i: calculate(x)

    # Creating buttons and placing them in the grid
    Button(text=i, font="verdana 8 bold", width=10, height=2, relief=GROOVE, command=command)\
        .grid(row=row, column=col)

    col += 1
    if col > 2:
        col = 0
        row += 1

window.mainloop()
