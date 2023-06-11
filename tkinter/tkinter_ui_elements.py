import tkinter as tk

labels = [
    "First Name:",
    "Last Name:",
    "Address Line 1:",
    "Address Line 2:",
    "City:",
    "State/Province:",
    "Postal Code:",
    "Country:",
]


window = tk.Tk()
window.title('Address Entry Form')

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

for index, label in enumerate(labels):
    lbls = tk.Label(master=frm_form, text=label)
    ents = tk.Entry(master=frm_form, width=50)

    lbls.grid(row=index, column=0, sticky="e")
    ents.grid(row=index, column=1)

frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, padx=5, pady=20)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=20)

btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT, ipadx=10)

window.mainloop()