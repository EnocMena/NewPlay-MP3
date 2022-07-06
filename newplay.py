"""
TODO LIST:
DONE - Change the background color of main tkinter window
- Add menu on the left side of tkinter window
"""

# import libraries
import tkinter as tk

# window
window = tk.Tk()
window.title("NewPlay")
window.geometry('1000x800')
window.minsize(1000, 800) # minimum size user can scale window
window.maxsize(1200, 1000) # maximum size user can scale window

# menu


# loop window
window.config(bg="orange") # background color
window.mainloop()
