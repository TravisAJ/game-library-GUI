#!/usr/bin/python3
# Taffea Avenevoli
# 02/10/20

import pickle as pk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

'''The Game Library Program'''

#------------- CONSTANTS -------------
TITLE_FONT = ("Times New Roman", 24)
LABEL_FONT = ("Times New Roman", 18)
ENTRY_FONT = ("Times New Roman", 15)
BUTTON_FONT = ("Arial", 15)
SCROLL_FONT = ("Arial", 12)

#----- SCREEN CLASS -----
class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)
    def switch_frame():
        screens[Screen.current].tkraise()
        
#----- MAIN MENU CLASS -----
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        
        self.lbl_main = tk.Label(self, text = "Welcome To The Game Library", font = TITLE_FONT)
        self.lbl_main.grid(row = 1, column = 1, columnspan=3, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "ADD", font = BUTTON_FONT, command = self.go_add)
        self.btn_add.grid(row = 2, column = 2, sticky = "news")
        
        self.btn_edit = tk.Button(self, text = "EDIT", font = BUTTON_FONT, command = self.go_edit)
        self.btn_edit.grid(row = 3, column = 2, sticky = "news")
        
        self.btn_search = tk.Button(self, text = "SEARCH", font = BUTTON_FONT, command = self.go_search)
        self.btn_search.grid(row = 4, column = 2, sticky = "nwes")
        
        self.btn_remove = tk.Button(self, text = "REMOVE", font = BUTTON_FONT, command = self.go_remove)
        self.btn_remove.grid(row = 5, column = 2, sticky = "news")
        
        self.btn_save = tk.Button(self, text = "SAVE", font = BUTTON_FONT, command = self.go_save)
        self.btn_save.grid(row = 6, column = 2, sticky = "news")
    
    def go_add(self):
        Screen.current = 1
        screens[Screen.current].reset_add()
        Screen.switch_frame()
        
    def go_edit(self):
        popup = tk.Tk()
        popup.title("Edit")
        frm_edit = EditPopup(popup)
        frm_edit.grid(row = 0, column = 0)
        
    def go_search(self):
        Screen.current = 3
        Screen.switch_frame()
        
    def go_remove(self):
        popup = tk.Tk()
        popup.title("Remove Menu")
        frm_remove = RemovePopup(popup)
        frm_remove.grid(row = 0, column = 0)      
        
    def go_save(self):
        messagebox.showinfo("Saved", "File Saved.")
        datafile = open("game_lib.pickle", "wb")
        pk.dump(games, datafile)
        datafile.close()

#----- ADD MENU CLASS -----        
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
        
        options = ["** SELECT GAMEMODE **", "Singleplayer", "Multiplayer", "Either"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_gamemode = tk.OptionMenu(self, self.tkvar, * options)
        self.dbx_gamemode.grid(row = 4, column = 4, columnspan = 3, sticky = "news")
        
        self.scr_notes = ScrolledText(self, width = 110, height = 7, font = SCROLL_FONT)
        self.scr_notes.grid(row = 5, column = 1, columnspan = 6)
        
        self.btn_cancel_add = tk.Button(self, text = "CANCEL", font = BUTTON_FONT, command = self.cancel_add)
        self.btn_cancel_add.grid(row = 6, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_reset = tk.Button(self, text = "RESET", font = BUTTON_FONT, command = self.reset_add)
        self.btn_reset.grid(row = 6, column = 3, columnspan = 2, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "ADD", font = BUTTON_FONT, command = self.submit_add)
        self.btn_add.grid(row = 6, column = 5, columnspan = 2, sticky = "news")
        
    def cancel_add(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def reset_add(self):
        self.ent_genre.delete(0, 'end')
        self.ent_title.delete(0, 'end')
        self.ent_developer.delete(0, 'end')
        self.ent_publisher.delete(0, 'end')
        self.ent_system.delete(0, 'end')
        self.ent_release.delete(0, 'end')
        self.ent_rating.delete(0, 'end')
        self.ent_price.delete(0, 'end')
        self.ent_purchase.delete(0, 'end')
        self.scr_notes.delete(0.0, 'end')
        
    def submit_add(self):
        if self.ent_title.get() == "":
            messagebox.showerror("¡ERROR!", "Please Insert Title")
        else:
            entry = []
            entry.append(self.ent_genre.get())
            entry.append(self.ent_title.get())
            entry.append(self.ent_developer.get())
            entry.append(self.ent_publisher.get())
            entry.append(self.ent_system.get())
            entry.append(self.ent_release.get())
            entry.append(self.ent_rating.get())
            entry.append(self.tkvar.get())
            entry.append(self.ent_price.get())
            entry.append("")
            entry.append(self.ent_purchase.get())
            entry.append(self.scr_notes.get(0.0, "end"))
            games[len(games)+1] = entry
            messagebox.showinfo("Success", "Game Added!")
            Screen.current = 0
            Screen.switch_frame()
                   
    def update(self):
        entry = games[self.edit_key]
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])
        self.ent_title.delete(0, "end")
        self.ent_title.insert(0, entry[1])
        self.ent_publisher.delete(0, "end")
        self.ent_publisher.insert(0, entry[2])
        self.ent_developer.delete(0, "end")
        self.ent_developer.insert(0, entry[3])
        self.ent_system.delete(0, "end")
        self.ent_system.insert(0, entry[4])
        self.ent_release.delete(0, "end")
        self.ent_release.insert(0, entry[5])
        self.ent_rating.delete(0, "end")
        self.ent_rating.insert(0, entry[6])
        self.ent_price.delete(0, "end")
        self.ent_price.insert(0, entry[8])
        self.ent_purchase.delete(0, "end")
        self.ent_purchase.insert(0, entry[10])
        self.scr_notes.delete(0.0, "end")
        self.scr_notes.insert(0.0, entry[11])
        
#----- EDIT SELECT CLASS -----
class EditPopup(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        
        self.lbl_edit = tk.Label(self, text = "Which title would you like to edit?", font = TITLE_FONT)
        self.lbl_edit.grid(row = 1, column = 1, columnspan = 4, sticky = "news")
        
        self.options = ["** SELECT A TITLE **"]
        for key in games:
            self.options.append(games[key][1])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.dbx_edit = tk.OptionMenu(self, self.tkvar, * self.options)
        self.dbx_edit.grid(row = 3, column = 1, columnspan = 4, sticky = "news")
        
        self.btn_cancel_edit = tk.Button(self, text = "CANCEL", font = BUTTON_FONT, command = self.cancel_edit)
        self.btn_cancel_edit.grid(row = 4, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_edit = tk.Button(self, text = "CONFIRM", font = BUTTON_FONT, command = self.submit_edit)
        self.btn_edit.grid(row = 4, column = 3, columnspan = 2, sticky = "news")    
        
    def cancel_edit(self):
        self.parent.destroy()
        
    def submit_edit(self):
        if self.tkvar.get() == self.options[0]:
            popup = tk.Tk()
            popup.title("!ERROR!")
            msg = "Error: Select a Title!"
            frm_error = PopMessage(popup, msg)
            frm_error.grid(row = 1, column = 1) 
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[2].edit_key = i
                    break
            Screen.current = 2
            screens[Screen.current].update()
            Screen.switch_frame()        
            self.parent.destroy()

#----- EDIT MENU CLASS -----
class EditMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
        
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
        
        options = ["** SELECT GAMEMODE **", "Singleplayer", "Multiplayer", "Either"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(options[0])
        self.dbx_gamemode = tk.OptionMenu(self, self.tkvar, * options)
        self.dbx_gamemode.grid(row = 4, column = 4, columnspan = 3, sticky = "news")
        
        self.scr_notes = ScrolledText(self, width = 110, height = 7, font = SCROLL_FONT)
        self.scr_notes.grid(row = 5, column = 1, columnspan = 6)
        
        self.btn_cancel_add = tk.Button(self, text = "CANCEL", font = BUTTON_FONT, command = self.cancel_edit)
        self.btn_cancel_add.grid(row = 6, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_reset = tk.Button(self, text = "RESET", font = BUTTON_FONT, command = self.reset_edit)
        self.btn_reset.grid(row = 6, column = 3, columnspan = 2, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "EDIT", font = BUTTON_FONT, command = self.submit_edit)
        self.btn_add.grid(row = 6, column = 5, columnspan = 2, sticky = "news")
        
    def cancel_edit(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def reset_edit(self):
        self.ent_genre.delete(0, 'end')
        self.ent_title.delete(0, 'end')
        self.ent_developer.delete(0, 'end')
        self.ent_publisher.delete(0, 'end')
        self.ent_system.delete(0, 'end')
        self.ent_release.delete(0, 'end')
        self.ent_rating.delete(0, 'end')
        self.ent_price.delete(0, 'end')
        self.ent_purchase.delete(0, 'end')
        self.scr_notes.delete(0.0, 'end')
        
    def submit_edit(self):
        if self.ent_title.get() == "":
            messagebox.showerror("¡ERROR!", "Title Can't Be Empty!")
        else:
            entry = []
            entry.append(self.ent_genre.get())
            entry.append(self.ent_title.get())
            entry.append(self.ent_developer.get())
            entry.append(self.ent_publisher.get())
            entry.append(self.ent_system.get())
            entry.append(self.ent_release.get())
            entry.append(self.ent_rating.get())
            entry.append(self.tkvar.get())
            entry.append(self.ent_price.get())
            entry.append("")
            entry.append(self.ent_purchase.get())
            entry.append(self.scr_notes.get(0.0, "end"))
            games[self.edit_key] = entry
            messagebox.showinfo("Success", "Game Edited!")
            Screen.current = 0
            Screen.switch_frame()
                   
    def update(self):
        entry = games[self.edit_key]
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])
        self.ent_title.delete(0, "end")
        self.ent_title.insert(0, entry[1])
        self.ent_publisher.delete(0, "end")
        self.ent_publisher.insert(0, entry[2])
        self.ent_developer.delete(0, "end")
        self.ent_developer.insert(0, entry[3])
        self.ent_system.delete(0, "end")
        self.ent_system.insert(0, entry[4])
        self.ent_release.delete(0, "end")
        self.ent_release.insert(0, entry[5])
        self.ent_rating.delete(0, "end")
        self.ent_rating.insert(0, entry[6])
        self.ent_price.delete(0, "end")
        self.ent_price.insert(0, entry[8])
        self.ent_purchase.delete(0, "end")
        self.ent_purchase.insert(0, entry[10])
        self.scr_notes.delete(0.0, "end")
        self.scr_notes.insert(0.0, entry[11])

#----- SEARCH MENU CLASS -----
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
        
        self.options = ["None", "Genre", "Title", "Developer", "Publisher", "System",
                   "Release Date", "Rating", "Gamemode", "Price", "Progress", "Purchase Date"]
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.dbx_search_by = tk.OptionMenu(self, self.tkvar, * self.options)
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
        
        self.btn_back = tk.Button(self, text = "BACK", font = BUTTON_FONT, command = self.cancel_search)
        self.btn_back.grid(row = 7, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_clear = tk.Button(self, text = "CLEAR", font = BUTTON_FONT, command = self.clear_search)
        self.btn_clear.grid(row = 7, column = 3, columnspan = 2, sticky = "news")
        
        self.btn_search = tk.Button(self, text = "SEARCH", font = BUTTON_FONT, command = self.submit_search)
        self.btn_search.grid(row = 7, column = 5, columnspan = 2, sticky = "news")
        
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
        self.scr_search.delete(0.0, 'end')
        
    def cancel_search(self):
        Screen.current = 0
        Screen.switch_frame()
        self.scr_search.delete(0.0, 'end')
        self.frm_print_filters.genre_var.set(True)
        self.frm_print_filters.title_var.set(True)
        self.frm_print_filters.developer_var.set(True)
        self.frm_print_filters.publisher_var.set(True)
        self.frm_print_filters.system_var.set(True)
        self.frm_print_filters.release_var.set(True)
        self.frm_print_filters.rating_var.set(True)
        self.frm_print_filters.gamemode_var.set(True)
        self.frm_print_filters.price_var.set(True)
        self.frm_print_filters.progress_var.set(True)
        self.frm_print_filters.purchase_var.set(True)
        self.frm_print_filters.notes_var.set(True)        
        
    def clear_search(self):
        self.ent_search_for.delete(0, 'end')
        
    def submit_search(self):
        self.scr_search.delete(0.0, 'end')
        self.print_search()
        
    def filter_print(self, entry):
        if self.frm_print_filters.genre_var.get() == True:
            msg = "Genre: " + entry[0] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.title_var.get() == True:
            msg = "Title: " + entry[1] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.developer_var.get() == True:
            msg = "Developer: " + entry[2] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.publisher_var.get() == True:
            msg = "Publisher: " + entry[3] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.system_var.get() == True:
            msg = "System: " + entry[4] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.release_var.get() == True:
            msg = "Release Year: " + entry[5] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.rating_var.get() == True:
            msg = "Personal Rating: " + entry[6] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.gamemode_var.get() == True:
            msg = "Gamemode: " + entry[7] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.price_var.get() == True:
            msg = "Price: " + entry[8] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.progress_var.get() == True:
            msg = "Beat It?: " + entry[9] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.purchase_var.get() == True:
            msg = "Purchase Date: " + entry[10] + "\n"
            self.scr_search.insert("insert", msg)
        if self.frm_print_filters.notes_var.get() == True:
            msg = "Notes: " + entry[11] + "\n"
            self.scr_search.insert("insert", msg)
        msg = "-----------------------------------------------------------\n"
        self.scr_search.insert("insert", msg)
    
    def print_search(self):
        keyword = self.ent_search_for.get()
        found = False
        self.scr_search.delete(0.0, "end")
        for key in games.keys( ):
            entry = games[key]
            if self.tkvar.get() == self.options[0]:
                self.filter_print(entry)
                found = True
                
            if self.tkvar.get() == self.options[1]:
                if keyword in entry[0]:
                    self.filter_print(entry)
                    found = True
                    
            if self.tkvar.get() == self.options[2]:
                if keyword in entry[1]:
                    self.filter_print(entry)
                    found = True
                    
            if self.tkvar.get() == self.options[3]:
                if keyword in entry[2]:
                    self.filter_print(entry)
                    found = True
                    
            if self.tkvar.get() == self.options[4]:
                if keyword in entry[3]:
                    self.filter_print(entry)
                    found = True
                    
            if self.tkvar.get() == self.options[5]:
                if keyword in entry[4]:
                    self.filter_print(entry)
                    found = True
                            
            if self.tkvar.get() == self.options[6]:
                if keyword in entry[5]:
                    self.filter_print(entry)
                    found = True
                            
            if self.tkvar.get() == self.options[7]:
                if keyword in entry[6]:
                    self.filter_print(entry)
                    found = True
                            
            if self.tkvar.get() == self.options[8]:
                if keyword in entry[7]:
                    self.filter_print(entry)
                    found = True
                    
            if self.tkvar.get() == self.options[9]:
                if keyword in entry[8]:
                    self.filter_print(entry)
                    found = True
                                    
            if self.tkvar.get() == self.options[10]:
                if keyword in entry[9]:
                    self.filter_print(entry)
                    found = True
                                    
            if self.tkvar.get() == self.options[11]:
                if keyword in entry[10]:
                    self.filter_print(entry)
                    found = True
                    
            if not found:
                messagebox.showwarning("Not Found", "No Results Found!")
                break
        
#----- SEARCH CHECKBOX CLASS -----
class PrintFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        
        self.genre_var = tk.BooleanVar(self, True)
        self.chk_genre = tk.Checkbutton(self, fg = "gray", variable = self.genre_var, text = "Genre")
        self.chk_genre.grid(row = 1, column = 1, sticky = "nsw")

        self.title_var = tk.BooleanVar(self, True) 
        self.chk_title = tk.Checkbutton(self, fg = "gray", variable = self.title_var, text = "Title")
        self.chk_title.grid(row = 2, column = 1, sticky = "nsw")

        self.developer_var = tk.BooleanVar(self, True)       
        self.chk_developer = tk.Checkbutton(self, fg = "gray", variable = self.developer_var, text = "Developer")
        self.chk_developer.grid(row = 3, column = 1, sticky = "nsw")

        self.publisher_var = tk.BooleanVar(self, True)     
        self.chk_publisher = tk.Checkbutton(self, fg = "gray", variable = self.publisher_var, text = "Publisher")
        self.chk_publisher.grid(row = 4, column = 1, sticky = "nsw")

        self.system_var = tk.BooleanVar(self, True)        
        self.chk_system = tk.Checkbutton(self, fg = "gray", variable = self.system_var, text = "System")
        self.chk_system.grid(row = 1, column = 2, sticky = "nsw")

        self.release_var = tk.BooleanVar(self, True)        
        self.chk_release = tk.Checkbutton(self, fg = "gray", variable = self.release_var, text = "Release")
        self.chk_release.grid(row = 2, column = 2, sticky = "nsw")

        self.rating_var = tk.BooleanVar(self, True)        
        self.chk_rating = tk.Checkbutton(self, fg = "gray", variable = self.rating_var, text = "Rating")
        self.chk_rating.grid(row = 3, column = 2, sticky = "nsw")

        self.gamemode_var = tk.BooleanVar(self, True)        
        self.chk_gamemode = tk.Checkbutton(self, fg = "gray", variable = self.gamemode_var, text = "Gamemode")
        self.chk_gamemode.grid(row = 4, column = 2, sticky = "nsw")

        self.price_var = tk.BooleanVar(self, True)
        self.chk_price = tk.Checkbutton(self, fg = "gray", variable = self.price_var, text = "Price")
        self.chk_price.grid(row = 1, column = 3, sticky = "nsw")

        self.progress_var = tk.BooleanVar(self, True)     
        self.chk_progress = tk.Checkbutton(self, fg = "gray", variable = self.progress_var, text = "Progress")
        self.chk_progress.grid(row = 2, column = 3, sticky = "nsw")

        self.purchase_var = tk.BooleanVar(self, True)
        self.chk_purchase = tk.Checkbutton(self, fg = "gray", variable = self.purchase_var, text = "Purchase")
        self.chk_purchase.grid(row = 3, column = 3, sticky = "nsw")

        self.notes_var = tk.BooleanVar(self, True)
        self.chk_notes = tk.Checkbutton(self, fg = "gray", variable = self.notes_var, text = "Notes")
        self.chk_notes.grid(row = 4, column = 3, sticky = "nsw")

#----- REMOVE MENU CLASS -----
class RemovePopup(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1) 
        
        self.lbl_edit = tk.Label(self, text = "Which title would you like to remove?", font = TITLE_FONT)
        self.lbl_edit.grid(row = 1, column = 1, columnspan = 4, sticky = "news")
        
        self.options = ["** SELECT A TITLE **"]
        for key in games:
            self.options.append(games[key][1])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])
        self.dbx_edit = tk.OptionMenu(self, self.tkvar, * self.options)
        self.dbx_edit.grid(row = 3, column = 1, columnspan = 4, sticky = "news")
        
        self.btn_cancel_remove = tk.Button(self, text = "CANCEL", font = BUTTON_FONT, command = self.cancel_remove)
        self.btn_cancel_remove.grid(row = 4, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_remove = tk.Button(self, text = "REMOVE", font = BUTTON_FONT, command = self.submit_remove)
        self.btn_remove.grid(row = 4, column = 3, columnspan = 2, sticky = "news")
        
    def cancel_remove(self):
        self.parent.destroy()
        
    def submit_remove(self):
        if self.tkvar.get() == self.options[0]:
            popup = tk.Tk()
            popup.title("¡ERROR!")
            msg = "Error: Select a Title!"
            frm_error = PopMessage(popup, msg)
            frm_error.grid(row = 1, column = 1) 
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[4].remove_key = i
                    break
            Screen.current = 4
            screens[Screen.current].update()
            Screen.switch_frame()        
            self.parent.destroy()
        
class RemoveMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.remove_key = 0
        
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)
        
        self.lbl_remove_1 = tk.Label(self, text = "Are you sure you want to delete this", font = TITLE_FONT)
        self.lbl_remove_1.grid(row = 1, column = 1, columnspan = 4, sticky = "news")
        
        self.lbl_remove_2 = tk.Label(self, text = "game with the following information?", font = TITLE_FONT)
        self.lbl_remove_2.grid(row = 2, column = 1, columnspan = 4, sticky = "news")
        
        self.scr_remove = ScrolledText(self, width = 110, height = 9.5, font = SCROLL_FONT)
        self.scr_remove.grid(row = 3, column = 1, columnspan = 4, sticky = "news") 
        
        self.btn_no = tk.Button(self, text = "NO", font = BUTTON_FONT, command = self.remove_no)
        self.btn_no.grid(row = 4, column = 1, columnspan = 2, sticky = "news")
        
        self.btn_yes = tk.Button(self, text = "YES", font = BUTTON_FONT, command = self.remove_yes)
        self.btn_yes.grid(row = 4, column = 3, columnspan = 2, sticky = "news")
        
    def remove_no(self):
        Screen.current = 0
        Screen.switch_frame()
        
    def remove_yes(self):
        for key in range(1, len(games) + 1):
            if key >= self.remove_key and key != len(games):
                games[key] = games[key + 1]
            if key == len(games):
                games.pop(key)
                messagebox.showinfo("Success", "Game removed!")
                Screen.current = 0
                Screen.switch_frame()        
    
    def update(self):
        entry = games[self.remove_key]
        msg = "Genre: " + entry[0] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Title: " + entry[1] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Developer: " + entry[2] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Publisher: " + entry[3] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "System: " + entry[4] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Release Date: " + entry[5] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Rating: " + entry[6] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Gamemode: " + entry[7] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Price: " + entry[8] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Beat it?: " + entry[9] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Purchase Date: " + entry[10] + "\n"
        self.scr_remove.insert("insert", msg)
        msg = "Notes: " + entry[11] + "\n"
        self.scr_remove.insert("insert", msg)        

#----- POPUP MESSAGE CLASS -----
class PopMessage(tk.Frame):
    def __init__ (self, parent, msg = "generic"):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        self.lbl_continue = tk.Label(self, text = msg, font = LABEL_FONT)
        self.lbl_continue.grid()
        
        self.btn_ok = tk.Button(self, text = "OK", command = self.parent.destroy, font = BUTTON_FONT)
        self.btn_ok.grid()
        
#---------- MAIN ----------
if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("The Game Library")
    
    screens = [MainMenu(), AddMenu(), EditMenu(), SearchMenu(), RemoveMenu()]
    
    screens[0].grid(row = 1, column = 1, sticky = "news")
    screens[1].grid(row = 1, column = 1, sticky = "news")
    screens[2].grid(row = 1, column = 1, sticky = "news")
    screens[3].grid(row = 1, column = 1, sticky = "news")
    screens[4].grid(row = 1, column = 1, sticky = "news")

    root.grid_columnconfigure(1, weight = 1)
    root.grid_rowconfigure(1, weight = 1)

main = screens[0]
main.tkraise()

root.mainloop()