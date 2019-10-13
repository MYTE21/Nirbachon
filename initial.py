import tkinter as tk


class Initial:
    def __init__(self, window):
        title = tk.Label(window, text="MYTE Nirbachon", fg="black", bg="yellow", font="Helvetica 16 bold italic").place(x=310, y=30)
        title.pack()
        w = tk.Canvas(window, width=400, height=400)
        w.pack()
