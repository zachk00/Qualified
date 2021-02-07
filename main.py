from tkinter import *
from tkinter import filedialog
import shutil
import data as da
import update as up
import Lookup as Lk

root = Tk()
root.title("Qualified")
root.iconbitmap("Resources/logo.ico")
states_var = StringVar(root)
states_var.set(" ")

global job_mapping
job_mapping = {}

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
        shutil.copyfile(root.filename, 'Documents/Cover_Letter.docx')


def search():
    search_criteria = {
        "title": title_input.get(),
        "experience": default_xp.get(),
        "city": city_input.get(),
        "state": states_var.get(),
        "skills": skills
    }
    status.config(text="Searching for Jobs Now!!!", bg="yellow")
    da.Jobs = Lk.lookup_jobs(search_criteria)
    search_complete()
    refresh()


def search_complete():
    global pop
    pop = Toplevel(root)
    pop.title("Job Search Complete")
    root.iconbitmap("Resources/logo.ico")
    pop.geometry("200x100")

    success = Label(pop, text=str(len(da.Jobs)) + " were found matching your search")
    success.grid(row=0, column=0)
    status.config(text="Click the search button once you're ready to start!", bg="white")


def export():
    root.filename = filedialog.askdirectory()
    up.write_listing(da.Jobs)
    if root.filename != "":
        shutil.copy("Documents/Qualified_Jobs.csv", root.filename)


def add_skill():
    skills.append(skill_entry.get())
    if skill_var.get() != "":
        skill_var.set(skill_var.get() + ", " + skill_entry.get())
    else:
        skill_var.set(skill_entry.get())


def refresh():
    job_var.set('')
    titles = []
    job_menu.children['menu'].delete(0, "end")
    for job in da.Jobs:
        titles.append(job.title)
        job_mapping[job.title] = job
    for title in titles:
        job_menu.children['menu'].add_command(label=title, command=lambda title_=title: job_var.set(title_))




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

export_bth = Button(root, text="Export Job List", width=30, command=export)
export_bth.grid(row=6, column=1, padx=10, pady=10)

job_var = StringVar()

update_cover_btn = Button(root, text="Update Cover Letter", width=30, command=lambda: up.update_cover_letter(job_mapping.get(job_var.get())))
update_cover_btn.grid(row=7, column=0, padx=10, pady=10)

job_menu = OptionMenu(root, job_var, [])
job_menu.grid(row=7, column=1, padx=10, pady=10)

status = Label(root, text="Click the search button once you're ready to start!", bd=1, relief=SUNKEN, bg="white")
status.grid(row=8, column=0, columnspan=4, sticky=W + E)

root.mainloop()
