import tkinter as tk


class TeamButton:
    def __init__(self, window):
        tk.Button(window, text="Button 1").place(x=90, y=50)
        tk.Button(window, text="Button 2").place(x=90, y=100)
