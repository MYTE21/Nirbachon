import tkinter as tk
import team_number
import team_button

window = tk.Tk()


def add():
    team_number.TeamNumber(window)
    team_button.TeamButton(window)


class Initial:
    def __init__(self):
        window.geometry('800x400')
        window.title("Bangladesh Nirbachon")
        add()


if __name__ == '__main__':
    Initial()
    window.mainloop()

