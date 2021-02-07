from tkinter import *
from tkinter import filedialog
import shutil
import data as da

root = Tk()
root.geometry("900x400")
# city and state input

city_label = Label(root, text="City")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_input = Entry(root, width=30)
city_input.grid(row=0, column=1, padx=10, pady=10)
city_input.insert(0, "i.e Gainesville")

states_var = StringVar(root)
states_var.set(" ")

state_label = Label(root, text="State")
state_label.grid(row=0, column=2, padx=10, pady=10)

state_dropdown = OptionMenu(root, states_var, *da.states_list)
state_dropdown.grid(row=0, column=3, padx=10, pady=10)

title_label = Label(root, text="Title")
title_label.grid(row=1, column=0, padx=10, pady=10)

title_input = Entry(root, width=30)
title_input.grid(row=1, column=1, padx=10, pady=10)
title_input.insert(0, "i.e Software Engineer")

xp_label = Label(root, text="Experience Level")

xp_label.grid(row=1, column=2, padx=10, pady=10)

default_xp = StringVar(root)
default_xp.set("Entry")

xp_dropdown = OptionMenu(root, default_xp, *da.XP_Levels)
xp_dropdown.grid(row=1, column=3, padx=10, pady=10)


def upload_file(item):
    root.filename = filedialog.askopenfilename(initialdir="C:\\", title="Select a File",
                                               filetypes=(("pdf Files", "*.pdf"), ("docx Files", "*.docx")))
    if root.filename != "":
        shutil.copy(root.filename, 'Documents')


def search():
    search_criteria = {
        "title": title_input.get(),
        "experience": default_xp.get(),
        "city": city_input.get(),
        "state": states_var.get()
    }

    # lookup_jobs(search_criteria)


search_btn = Button(root, text="Search", width=30, command=search)
search_btn.grid(row=3, column=1, padx=10, pady=10)

upload_cover_ltr_btn = Button(root, text="Upload Cover Letter", width=30, command=lambda: upload_file("coverL"))
upload_cover_ltr_btn.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
