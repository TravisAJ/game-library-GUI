#!/usr/bin/python3
# Taffea Avenevoli
# 02/10/20

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

'''The Game Library Program'''

TITLE_FONT = ("Times New Roman", 24)
LABEL_FONT = ("Times New Roman", 18)
ENTRY_FONT = ("Times New Roman", 15)
BUTTON_FONT = ("Arial", 15)
SCROLL_FONT = ("Arial", 12)

class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        
        self.lbl_main = tk.Label(self, text = "The Game Library", font = TITLE_FONT)
        self.lbl_main.grid(row = 1, column = 1, columnspan=3, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "ADD", font = BUTTON_FONT)
        self.btn_add.grid(row = 2, column = 2, sticky = "news")
        
        self.btn_edit = tk.Button(self, text = "EDIT", font = BUTTON_FONT)
        self.btn_edit.grid(row = 3, column = 2, sticky = "nwes")
        
        self.btn_search = tk.Button(self, text = "SEARCH", font = BUTTON_FONT)
        self.btn_search.grid(row = 4, column = 2, sticky = "nwes")
        
        self.btn_remove = tk.Button(self, text = "REMOVE", font = BUTTON_FONT)
        self.btn_remove.grid(row = 5, column = 2, sticky = "news")
        
        self.btn_save = tk.Button(self, text = "SAVE", font = BUTTON_FONT)
        self.btn_save.grid(row = 6, column = 2, sticky = "news")
        
class AddMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)        
        
        self.lbl_genre = tk.Label(self, text = "Genre:", font = LABEL_FONT)
        self.lbl_genre.grid(row = 1, column = 1, sticky = "news")
        
        self.ent_genre = tk.Entry(self, font = ENTRY_FONT)
        self.ent_genre.grid(row = 1, column = 2, sticky = "news")
        
        self.lbl_title = tk.Label(self, text = "Title:", font = LABEL_FONT)
        self.lbl_title.grid(row = 1, column = 3, sticky = "news")
        
        self.ent_title = tk.Entry(self, font = ENTRY_FONT)
        self.ent_title.grid(row = 1, column = 4, sticky = "news")
        
        self.lbl_developer = tk.Label(self, text = "Developer:", font = LABEL_FONT)
        self.lbl_developer.grid(row = 1, column = 5, sticky = "news")
        
        self.ent_developer = tk.Entry(self, font = ENTRY_FONT)
        self.ent_developer.grid(row = 1, column = 6, sticky = "news")
        
        self.lbl_publisher = tk.Label(self, text = "Publisher:", font = LABEL_FONT)
        self.lbl_publisher.grid(row = 2, column = 1, sticky = "news")
        
        self.ent_publisher = tk.Entry(self, font = ENTRY_FONT)
        self.ent_publisher.grid(row = 2, column = 2, sticky = "news")
        
        self.lbl_system = tk.Label(self, text = "System:", font = LABEL_FONT)
        self.lbl_system.grid(row = 2, column = 3, sticky = "news")
        
        self.ent_system = tk.Entry(self, font = ENTRY_FONT)
        self.ent_system.grid(row = 2, column = 4, sticky = "news")
        
        self.lbl_release = tk.Label(self, text = "Release Date:", font = LABEL_FONT)
        self.lbl_release.grid(row = 2, column = 5, sticky = "news")
        
        self.ent_release = tk.Entry(self, font = ENTRY_FONT)
        self.ent_release.grid(row = 2, column = 6, sticky = "news")
        
        self.lbl_rating = tk.Label(self, text = "Rating:", font = LABEL_FONT)
        self.lbl_rating.grid(row = 3, column = 1, sticky = "news")
        
        self.ent_rating = tk.Entry(self, font = ENTRY_FONT)
        self.ent_rating.grid(row = 3, column = 2, sticky = "news")
        
        self.lbl_price = tk.Label(self, text = "Price:", font = LABEL_FONT)
        self.lbl_price.grid(row = 3, column = 3, sticky = "news")
        
        self.ent_price = tk.Entry(self, font = ENTRY_FONT)
        self.ent_price.grid(row = 3, column = 4, sticky = "news")
        
        self.lbl_purchase = tk.Label(self, text = "Purchase Date:", font = LABEL_FONT)
        self.lbl_purchase.grid(row = 3, column = 5, sticky = "news")
        
        self.ent_purchase = tk.Entry(self, font = ENTRY_FONT)
        self.ent_purchase.grid(row = 3, column = 6, sticky = "news")
        
        self.lbl_progress = tk.Label(self, text = "Beat It?", font = LABEL_FONT)
        self.lbl_progress.grid(row = 4, column = 1, sticky = "news")
        
        self.chk_progress = tk.Checkbutton(self, fg = "gray")
        self.chk_progress.grid(row = 4, column = 2, sticky = "nsw")
        
        self.lbl_gamemode = tk.Label(self, text = "Gamemode:", font = LABEL_FONT)
        self.lbl_gamemode.grid(row = 4, column = 3, sticky = "news")
        
        options = ["Singleplayer", "Multiplayer", "Either"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.dbx_gamemode = tk.OptionMenu(self, tkvar, * options)
        self.dbx_gamemode.grid(row = 4, column = 4, columnspan = 3, sticky = "news")
        
        self.scr_notes = ScrolledText(self, width = 110, height = 5, font = SCROLL_FONT)
        self.scr_notes.grid(row = 5, column = 1, columnspan = 6)
        
        self.btn_cancel_add = tk.Button(self, text = "CANCEL", font = BUTTON_FONT)
        self.btn_cancel_add.grid(row = 6, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_reset = tk.Button(self, text = "RESET", font = BUTTON_FONT)
        self.btn_reset.grid(row = 6, column = 3, columnspan = 2, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "ADD", font = BUTTON_FONT)
        self.btn_add.grid(row = 6, column = 5, columnspan = 2, sticky = "news")
        
class EditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        
        self.lbl_edit = tk.Label(self, text = "Which title would you like to edit?", font = TITLE_FONT)
        self.lbl_edit.grid(row = 1, column = 1, columnspan = 4, sticky = "news")
        
        options = []
        for key in games:
            options.append(games[key][1])
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.dbx_edit = tk.OptionMenu(self, tkvar, * options)
        self.dbx_edit.grid(row = 3, column = 1, columnspan = 4, sticky = "news")
        
        self.btn_cancel_edit = tk.Button(self, text = "CANCEL", font = BUTTON_FONT)
        self.btn_cancel_edit.grid(row = 4, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_edit = tk.Button(self, text = "EDIT", font = BUTTON_FONT)
        self.btn_edit.grid(row = 4, column = 3, columnspan = 2, sticky = "news")
        
class SearchMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        self.grid_columnconfigure(5,weight=1)
        self.grid_columnconfigure(6,weight=1)
        
        self.lbl_search = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_search.grid(row = 1, column = 1, columnspan = 2, sticky = "news")
        
        self.lbl_search_by = tk.Label(self, text = "Search by:", font = LABEL_FONT)
        self.lbl_search_by.grid(row = 2, column = 1, columnspan = 2, sticky = "nsw")
        
        options = ["Genre", "Title", "Developer", "Publisher", "System",
                   "Release", "Rating", "Gamemode", "Price", "Progress", "Purchase"]
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.dbx_search_by = tk.OptionMenu(self, tkvar, * options)
        self.dbx_search_by.grid(row = 3, column = 1, columnspan = 2, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text = "Search for:", font = LABEL_FONT)
        self.lbl_search_for.grid(row = 4, column = 1, columnspan = 2, sticky = "nsw")
        
        self.ent_search_for = tk.Entry(self, font = ENTRY_FONT)
        self.ent_search_for.grid(row = 5, column = 1, columnspan = 2, sticky = "news")
        
        self.lbl_print_filters = tk.Label(self, text = "Print Filters:", font = TITLE_FONT)
        self.lbl_print_filters.grid(row = 1, column = 4, columnspan = 4, sticky = "news")
            
        self.frm_print_filters = PrintFilters(self)
        self.frm_print_filters.grid(row = 2, column = 4, columnspan = 3, rowspan = 4, sticky = "nesw")
        
        self.scr_search = ScrolledText(self, width = 110, height = 5, font = SCROLL_FONT)
        self.scr_search.grid(row = 6, column = 1, columnspan = 6)
        
        self.btn_back = tk.Button(self, text = "BACK", font = BUTTON_FONT)
        self.btn_back.grid(row = 7, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", font = BUTTON_FONT)
        self.btn_clear.grid(row = 7, column = 3, columnspan = 2, sticky = "news")
        
        self.btn_submit = tk.Button(self, text = "SUBMIT", font = BUTTON_FONT)
        self.btn_submit.grid(row = 7, column = 5, columnspan = 2, sticky = "news")        
        
class PrintFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        
        self.chk_genre = tk.Checkbutton(self, fg = "gray", text = "Genre")
        self.chk_genre.grid(row = 1, column = 1, sticky = "nsw")
        
        self.chk_title = tk.Checkbutton(self, fg = "gray", text = "Title")
        self.chk_title.grid(row = 2, column = 1, sticky = "nsw")
        
        self.chk_developer = tk.Checkbutton(self, fg = "gray", text = "Developer")
        self.chk_developer.grid(row = 3, column = 1, sticky = "nsw")
        
        self.chk_publisher = tk.Checkbutton(self, fg = "gray", text = "Publisher")
        self.chk_publisher.grid(row = 4, column = 1, sticky = "nsw")
        
        self.chk_system = tk.Checkbutton(self, fg = "gray", text = "System")
        self.chk_system.grid(row = 1, column = 2, sticky = "nsw")
        
        self.chk_release = tk.Checkbutton(self, fg = "gray", text = "Release")
        self.chk_release.grid(row = 2, column = 2, sticky = "nsw")
        
        self.chk_rating = tk.Checkbutton(self, fg = "gray", text = "Rating")
        self.chk_rating.grid(row = 3, column = 2, sticky = "nsw")
        
        self.chk_gamemode = tk.Checkbutton(self, fg = "gray", text = "Gamemode")
        self.chk_gamemode.grid(row = 4, column = 2, sticky = "nsw")
        
        self.chk_price = tk.Checkbutton(self, fg = "gray", text = "Price")
        self.chk_price.grid(row = 1, column = 3, sticky = "nsw")
        
        self.chk_progress = tk.Checkbutton(self, fg = "gray", text = "Progress")
        self.chk_progress.grid(row = 2, column = 3, sticky = "nsw")
        
        self.chk_purchase = tk.Checkbutton(self, fg = "gray", text = "Purchase")
        self.chk_purchase.grid(row = 3, column = 3, sticky = "nsw")
        
        self.chk_notes = tk.Checkbutton(self, fg = "gray", text = "Notes")
        self.chk_notes.grid(row = 4, column = 3, sticky = "nsw")
        
class RemoveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1) 
        
        self.lbl_edit = tk.Label(self, text = "Which title would you like to remove?", font = TITLE_FONT)
        self.lbl_edit.grid(row = 1, column = 1, columnspan = 4, sticky = "news")
        
        options = []
        for key in games:
            options.append(games[key][1])
        tkvar = tk.StringVar(self)
        tkvar.set(options[0])
        self.dbx_edit = tk.OptionMenu(self, tkvar, * options)
        self.dbx_edit.grid(row = 3, column = 1, columnspan = 4, sticky = "news")
        
        self.btn_cancel_remove = tk.Button(self, text = "CANCEL", font = BUTTON_FONT)
        self.btn_cancel_remove.grid(row = 4, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_remove = tk.Button(self, text = "REMOVE", font = BUTTON_FONT)
        self.btn_remove.grid(row = 4, column = 3, columnspan = 2, sticky = "news")
        
class SaveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)        
        
        self.lbl_save = tk.Label(self, text = "File saved.", font = TITLE_FONT)
        self.lbl_save.grid(row = 1, column = 1, columnspan = 3)
        
        self.btn_save = tk.Button(self, text = "OK", font = BUTTON_FONT)
        self.btn_save.grid(row = 2, column = 1, columnspan = 3)        

if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("The Game Library")
    
    screens = [MainMenu(), AddMenu(), EditMenu(),
               SearchMenu(), RemoveMenu(), SaveMenu()]  
    
    screens[0].grid(row = 0, column = 0, sticky = "nesw")
    screens[1].grid(row = 0, column = 0, sticky = "nesw")
    screens[2].grid(row = 0, column = 0, sticky = "nesw")
    screens[3].grid(row = 0, column = 0, sticky = "nesw")
    screens[4].grid(row = 0, column = 0, sticky = "nesw")
    screens[5].grid(row = 0, column = 0, sticky = "nesw")

    '''Temporary for ALPHA testing'''
    keep_going = True
    while keep_going:
        print("""
        Welcome to The Game Library View 
        --------------------------------
        1) Main Menu
        2) Add Menu
        3) Edit Menu
        4) Search Menu
        5) Remove Menu
        6) Save Menu
        """)
        
        selection = input("Pick a screen. ")
        if selection == "1":
            frame = screens[0]
            keep_going = False
        elif selection == "2":
            frame = screens[1]
            keep_going = False
        elif selection == "3":
            frame = screens[2]
            keep_going = False
        elif selection == "4":
            frame = screens[3]
            keep_going = False
        elif selection == "5":
            frame = screens[4]
            keep_going = False
        elif selection == "6":
            frame = screens[5]
            keep_going = False
        else:
            print("***INVALID INPUT***")

root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)

frame.tkraise()

root.mainloop()