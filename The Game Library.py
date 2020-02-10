#!/usr/bin/python3
# Taffea Avenevoli
# 02/10/20

import pickle as pk
import tkinter as tk
from tkinter import scrolledtext

'''The Game Library Program'''

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        lbl_title = tk.Label(text = "Game Library", font = TITLE_FONT)
        lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        btn_add = tk.Button(text = "ADD", font = BUTTON_FONT)
        btn_add.grid(row = 1, column = 0)
        
        btn_add = tk.Button(text = "EDIT", font = BUTTON_FONT)
        btn_add.grid(row = 2, column = 0)
        
        btn_add = tk.Button(text = "SEARCH", font = BUTTON_FONT)
        btn_add.grid(row = 3, column = 0)
        
        btn_add = tk.Button(text = "REMOVE", font = BUTTON_FONT)
        btn_add.grid(row = 4, column = 0)
        
        btn_add = tk.Button(text = "SAVE", font = BUTTON_FONT)
        btn_add.grid(row = 5, column = 0)        

if __name__ == "__main__":
    games = {}
    datafile = open("game_lib.pickle", "rb")
    games = pk.load(datafile)
    datafile.close()
    root = tk.Tk()
    root.title("The Game Library")
    root.geometry("500x500")
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0, sticky = "news")
    
    root.mainloop()
