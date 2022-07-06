"""
TODO LIST:
- Change the background color of main tkinter window
- Add a button to the window and test it works
"""

# import libraries
import tkinter as tk

# window
window = tk.Tk()
window.title("NewPlay")
window.geometry('1000x800')
window.minsize(1000, 800) # minimum size user can scale window
window.maxsize(1200, 1000) # maximum size user can scale window

# test widget
testWidget = tk.Label(text="Press me")
testWidget.pack()

# loop window
window.config(bg="red") # background color
window.mainloop()
