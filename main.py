from tkinter import *
from tkinter import filedialog
import shutil
import data as da

root = Tk()

states_var = StringVar(root)
states_var.set(" ")

default_xp = StringVar(root)
default_xp.set("Entry")

# city and state input
skills = []
city_label = Label(root, text="City")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_input = Entry(root, width=30)
city_input.grid(row=0, column=1, padx=10, pady=10)
city_input.insert(0, "i.e Gainesville")

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

xp_dropdown = OptionMenu(root, default_xp, *da.XP_Levels)
xp_dropdown.grid(row=1, column=3, padx=10, pady=10)


def upload_file():
    root.filename = filedialog.askopenfilename(initialdir="C:\\", title="Select a File",
                                               filetypes=(("pdf Files", "*.pdf"), ("docx Files", "*.docx")))
    if root.filename != "":
        shutil.copy(root.filename, 'Documents')


def search():
    search_criteria = {
        "title": title_input.get(),
        "experience": default_xp.get(),
        "city": city_input.get(),
        "state": states_var.get(),
        "skills": skills
    }

    # lookup_jobs(search_criteria)


def export_jobs():
    pass


def get_job_total():
    pass


def add_skill():
    skills.append(skill_entry.get())
    if skill_var.get() != "":
        skill_var.set(skill_var.get() + ", " + skill_entry.get())
    else:
        skill_var.set(skill_entry.get())


add_skill_btn = Button(root, text="Add a Skill", command=add_skill)
add_skill_btn.grid(row=3, column=0, padx=10, pady=10)

skill_entry = Entry(root, width=30)
skill_entry.grid(row=3, column=1, padx=10, pady=10)

skill_var = StringVar()

skills_l = Label(root, textvariable=skill_var)
skills_l.grid(row=3, column=2, padx=10, pady=10)

search_btn = Button(root, text="Search", width=30, command=search)
search_btn.grid(row=4, column=1, padx=10, pady=10)

upload_cover_ltr_btn = Button(root, text="Upload Cover Letter", width=30, command=upload_file)
upload_cover_ltr_btn.grid(row=5, column=1, padx=10, pady=10)

export_bth = Button(root, text="Export Job List", width=30, command=export_jobs)
export_bth.grid(row=6, column=1, padx=10, pady=10)

status = Label(root, text=str(len("temp")) + " Jobs Found", bd=1, relief=SUNKEN, anchor=E)
status.grid(row=7, column=0, columnspan=4, sticky=W + E)

update_cover_btn = Button()


root.mainloop()
