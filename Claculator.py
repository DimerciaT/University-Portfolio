from tkinter import *

window = Tk()
window.geometry("300x200")
window.title("Calculator")

icon = PhotoImage(file='calculator_icon.png')
window.iconphoto(True, icon)

window.mainloop()