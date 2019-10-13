import tkinter as tk
import initial

window = tk.Tk()


def add():
    initial.Initial(window)


class Initial:
    def __init__(self):
        window.geometry('800x400')
        window.title("MYTE Nirbachon")
        add()


if __name__ == '__main__':
    Initial()
    window.mainloop()

