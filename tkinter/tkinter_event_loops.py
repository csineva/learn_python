import tkinter as tk
from random import randint


def roll():
    lbl_value["text"] = randint(1, 6)


window = tk.Tk()

window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=50, weight=1)

btn_roll =  tk.Button(master=window, text="Roll", command=roll)
lbl_value = tk.Label(master=window, text="-")

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_value.grid(row=1, column=0, sticky="nsew")

window.mainloop()
