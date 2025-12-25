from tkinter import *

# Function to add value to screen
def press(value):
    display.insert(END, value)

# Function to clear screen
def clear():
    display.delete(0, END)

# Function to calculate result
def equal():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(END, result)
    except:
        display.delete(0, END)
        display.insert(END, "Error")

# Create window
window = Tk()
window.title("Calculator")
window.geometry("300x400")
icon = PhotoImage(file='calculator_icon.png')
window.iconphoto(True, icon)
window.config(bg="pink")

# Display
display = Entry(window, font=("Arial", 20), justify="right")
display.pack(fill=X, padx=10, pady=10)

# Buttons frame
frame = Frame(window)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        Button(frame, text=button, width=10, height=2, command=equal)\
            .grid(row=row, column=col, columnspan=2)
        col += 1
    else:
        Button(frame, text=button, width=5, height=2,
               command=lambda b=button: press(b))\
            .grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
Button(window, text="Clear", width=20, height=2, command=clear)\
    .pack(pady=10)

# Run app
window.mainloop()
