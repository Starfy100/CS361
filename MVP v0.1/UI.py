import tkinter as tk
import tkinter.tix as tkt
from idlelib.tooltip import Hovertip

def Search(event):
    print("Entering Search")


def Sort(event):
    print("Entering Sort")

def Admin(event):
    print("Entering Admin")
   



isRunning = False
print("Welcome to the Computer Components Compendium!")

window = tk.Tk()
window.columnconfigure([0,1,2,3,4], weight=1, minsize=150)
window.rowconfigure([0,1,2,3,4], weight=1, minsize=150)

title = tk.Label(text="Welcome to the\nComputer Components Compendium!")
title.grid(row = 0, column = 2)
#title.pack()

Help = tk.Label(
    window,text='Need Help? \n(Hover over me!)',
    width=25,
    height=15,
)
Help.grid(row = 0, column = 0)

SearchButton = tk.Button(
    text="Search",
    width=15,
    height=5,
    bg="blue",
    fg="white",
    
)
SearchButton.bind("<Button-1>", Search)
SearchButton.grid(row = 1, column = 1)

#SearchButton.pack()

SortButton = tk.Button(
    text="Sort",
    width=15,
    height=5,
    bg="green",
    fg="white",

)
SortButton.bind("<Button-1>", Sort)
SortButton.grid(row = 1, column = 3)
#SortButton.pack()

AdminButton = tk.Button(
    text="Admin",
    width=15,
    height=5,
    bg="Red",
    fg="yellow",

)
AdminButton.bind("<Button-1>", Admin)
AdminButton.grid(row = 0, column = 4)

AdminTip = Hovertip(AdminButton,'Clicking this button will enter Admin mode.\nDo NOT use this unless you have the Admin password', hover_delay=100)
SearchTip = Hovertip(SearchButton,'Clicking this button\nwill enter Search mode.', hover_delay=100)
SortTip = Hovertip(SortButton,'Clicking this button\nwill enter Sort mode.', hover_delay=100)
HelpTip = Hovertip(Help,'Search: Search allows you to search for a part by name\n(Try searching "RTX 3080 Ti")\nSort: Sort allows you to filter parts by characteristic\n(Try sorting by Price)\nAdmin: Admin allows for the direct editing of parts', hover_delay=100)
#tip = tkt.Balloon(window)
#tip.bind_widget(AdminButton,balloonmsg="Test Message")
#AdminButton.pack()


window.mainloop()
