import tkinter as tk

window = tk.Tk()

window.title("Add label with click")

user_input = tk.StringVar()
frm_buttons = tk.Frame()
frm_buttons.grid(row=0, column=0)
frm_labels = tk.Frame()
frm_labels.grid(row=1, column=0)

def add_label(s):
    tk.Label(frm_labels, text=s).pack()

# event=None to work both with command and bind (as bind sends 1 arg, the event itsel, command sends no arg)
def get_input(event=None):
    add_label(ent.get())

# detecting the bind keysym code
# def func(event):
#     print
#     event.keysym


a = "alma"
tk.Button(frm_buttons, text="Add label", command=lambda: add_label(a)).grid(row=0, column=0)
tk.Button(frm_buttons, text="Add input", command=lambda: get_input()).grid(row=0, column=1, )
ent = tk.Entry(frm_buttons, width=10)
ent.grid(row=1, columnspan=2)
ent.focus()
ent.bind("<Return>", get_input)


window.mainloop()