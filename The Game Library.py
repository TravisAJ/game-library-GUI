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

'''class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        lbl_title = tk.Label(text = "The Game Library", font = TITLE_FONT)
        lbl_title.grid(row = 1, column = 1, sticky = "news")
        
        btn_add = tk.Button(text = "ADD", font = BUTTON_FONT)
        btn_add.grid(row = 2, column = 1)
        
        btn_edit = tk.Button(text = "EDIT", font = BUTTON_FONT)
        btn_edit.grid(row = 3, column = 1)
        
        btn_search = tk.Button(text = "SEARCH", command = raise_search, font = BUTTON_FONT)
        btn_search.grid(row = 4, column = 1)
        
        btn_remove = tk.Button(text = "REMOVE", font = BUTTON_FONT)
        btn_remove.grid(row = 5, column = 1)
        
        btn_save = tk.Button(text = "SAVE", font = BUTTON_FONT)
        btn_save.grid(row = 6, column = 1)
        
    def raise_search(self):
        search_menu.tkraise()'''
        
class SearchMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_search = tk.Label(self, text = "Search", font = TITLE_FONT)
        self.lbl_search.grid(row = 1, column = 1, columnspan = 2, sticky = "news")
        
        self.lbl_search_by = tk.Label(self, text = "Search by:", font = LABEL_FONT)
        self.lbl_search_by.grid(row = 2, column = 1, columnspan = 2, sticky = "news")
        
        '''Temporarily An Entry, Change to Dropdown'''
        self.ent_search_by = tk.Entry(self, font = ENTRY_FONT)
        self.ent_search_by.grid(row = 3, column = 1, columnspan = 2, sticky = "news")
        
        self.lbl_search_for = tk.Label(self, text = "Search for:", font = LABEL_FONT)
        self.lbl_search_for.grid(row = 4, column = 1, columnspan = 2, sticky = "news")
        
        self.ent_search_for = tk.Entry(self, font = ENTRY_FONT)
        self.ent_search_for.grid(row = 5, column = 1, columnspan = 2, sticky = "news")
        
        self.lbl_print_filters = tk.Label(self, text = "Print Filters:", font = TITLE_FONT)
        self.lbl_print_filters.grid(row = 1, column = 4, columnspan = 4, sticky = "news")
            
        self.print_filters = PrintFilters(self)
        self.print_filters.grid(row = 2, column = 4, columnspan = 3, rowspan = 4, sticky = "news")
        
        self.scr_search = ScrolledText(self, font = SCROLL_FONT)
        self.scr_search.grid(row = 6, column = 1, columnspan = 6, sticky = "news")
        
        self.btn_back = tk.Button(self, text = "BACK", font = BUTTON_FONT)
        self.btn_back.grid(row = 7, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", font = BUTTON_FONT)
        self.btn_clear.grid(row = 7, column = 3, columnspan = 2, sticky = "news")
        
        self.btn_submit = tk.Button(self, text = "SUBMIT", font = BUTTON_FONT)
        self.btn_submit.grid(row = 7, column = 5, columnspan = 2, sticky = "news")        
        
class PrintFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.chk_genre = tk.Checkbutton(self, text = "Genre")
        self.chk_genre.grid(row = 1, column = 1, sticky = "news")
        
        self.chk_title = tk.Checkbutton(self, text = "Title")
        self.chk_title.grid(row = 2, column = 1, sticky = "news")
        
        self.chk_developer = tk.Checkbutton(self, text = "Developer")
        self.chk_developer.grid(row = 3, column = 1, sticky = "news")
        
        self.chk_publisher = tk.Checkbutton(self, text = "Publisher")
        self.chk_publisher.grid(row = 4, column = 1, sticky = "news")
        
        self.chk_system = tk.Checkbutton(self, text = "System")
        self.chk_system.grid(row = 1, column = 2, sticky = "news")
        
        self.chk_release = tk.Checkbutton(self, text = "Release")
        self.chk_release.grid(row = 2, column = 2, sticky = "news")
        
        self.chk_rating = tk.Checkbutton(self, text = "Rating")
        self.chk_rating.grid(row = 3, column = 2, sticky = "news")
        
        self.chk_gamemode = tk.Checkbutton(self, text = "Gamemode")
        self.chk_gamemode.grid(row = 4, column = 2, sticky = "news")
        
        self.chk_price = tk.Checkbutton(self, text = "Price")
        self.chk_price.grid(row = 1, column = 3, sticky = "news")
        
        self.chk_progress = tk.Checkbutton(self, text = "Progress")
        self.chk_progress.grid(row = 2, column = 3, sticky = "news")
        
        self.chk_purchase = tk.Checkbutton(self, text = "Purchase")
        self.chk_purchase.grid(row = 3, column = 3, sticky = "news")
        
        self.chk_notes = tk.Checkbutton(self, text = "Notes")
        self.chk_notes.grid(row = 4, column = 3, sticky = "news")                                                                                                

if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("The Game Library")
    #root.geometry("500x500")
    #main_menu = MainMenu()
    #main_menu.grid(row = 0, column = 0, sticky = "news")   
    
    search_menu = SearchMenu()
    search_menu.grid(row = 0, column = 0, sticky = "news")
    
    #main_menu.tkraise()
    root.mainloop()
