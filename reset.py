import pickle
import tkinter as tk
from tkinter import messagebox

games = {1:['Rhythm', 'Beat Saber', 'Beat Games', 'Oculus', 'Virtual Reality', 
            '2018', '10', 'Singleplayer', '30.00', 'No', '12/25/19', 'My favorite VR Game!'], 
         2:['Action', 'Just Shapes and Beats', 'Berzerk Studio', 'Steam', 'Windows',
            '2018', '9', 'Either', '20.00', 'Yes', '7/31/19', 'Great Music!'], 
         3:['MOBA', 'Brawl Stars', 'Supercell', 'Supercell', 'Android',
            '2017', '8.5', 'Multiplayer', 'Free', 'Yes', '12/12/18', 'The best mobile game!'],
         4:['Action-Adventure', 'Lego Star Wars', 'Travellers Tales', 'LucasArts', 'Xbox One',
            '2007', '7', 'Single', '20.00', 'No', '1/10/20', 'Hmmmmmm....herrrrrmmmmm']
         }

LABEL_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Times New Roman", 18)

class Reset_Frame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid_columnconfigure(1,weight=1)
    
        self.lbl_reset = tk.Label(self, text = "CONFIRM RESET?", font = LABEL_FONT)
        self.lbl_reset.grid(row = 1, column = 1, sticky = "news")
    
        self.btn_reset = tk.Button(self, text = "Confirm", font = BUTTON_FONT, command = self.reset)
        self.btn_reset.grid(row = 2, column = 1, sticky = "news")    

    def reset(self):
        datafile = open("game_lib.pickle", "wb")
        pickle.dump(games, datafile)
        datafile.close()
        messagebox.showinfo(message = "Data Reseted. Go Back to the Game Library.")
    
root = tk.Tk()
root.title("Data Reset")
    
main = Reset_Frame()
main.grid(row = 0, column = 0, sticky = "news")
main.tkraise()
    
root.mainloop()