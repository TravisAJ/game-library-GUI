#!/usr/bin/python3
# Taffea Avenevoli
# 02/10/20

import pickle as pk
import tkinter as tk

'''The Game Library Program'''

TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

games = {}
datafile = open("game_lib.pickle", "rb")
games = pk.load(datafile)
datafile.close()
