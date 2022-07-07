"""
TODO LIST:
DONE - Change the background color of main tkinter window
Done - Add menubar
- Start coding artist search window function
"""

# import libraries
import tkinter as tk
from tkinter import Menu
from youtubesearchpython import VideosSearch
from pprint import pprint

# window
window = tk.Tk()
window.title("NewPlay")
window.geometry('1000x800')
window.minsize(1000, 800) # minimum size user can scale window
window.maxsize(1200, 1000) # maximum size user can scale window

# search by artist window
def artist_search_window():
    print("This is a placeholder")

# menubar
def menu_bar():
    # menubar
    menuBar = Menu(window)
    window.config(menu=menuBar)

#############################SearchMusicMenu#############################
    # creates search menu
    search_menu = Menu(menuBar, tearoff=False)

    # add menu items to search menu
    search_menu.add_command(label='By Artist')
    search_menu.add_command(label='By Genre')
    search_menu.add_command(label='By Year')

    # add search menu to menubar
    menuBar.add_cascade(
        label="Search Music",
        menu=search_menu
    )
#########################################################################

#############################TrendingMenu################################
    # creates search menu
    trending_menu = Menu(menuBar, tearoff=False)

    # add menu items to search menu
    trending_menu.add_command(label='Top 10')
    trending_menu.add_command(label='Top 25')
    trending_menu.add_command(label='Top 40')

    # add search menu to menubar
    menuBar.add_cascade(
        label="Trending Songs",
        menu=trending_menu
    )
#########################################################################

# end of menubar

# loop window
menu_bar()
window.config(bg="orange") # background color
window.mainloop()
