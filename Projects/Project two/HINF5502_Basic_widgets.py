# HINF 5502: Program snippets: Basic Python GUI widgets
#
# Here are some short(ish) program snippets on Graphic User Interfaces (GUIs).
# For best results, be sure to run each of them in their own
# window as a program, rather than typing them in one line at a
# time in IDLE's interactive window.
#

# Here is an example using checkbuttons.
from Tkinter import *
root = Tk()
root.title("Checkbutton Test")
checkvar1 = StringVar()
checkvar2 = StringVar()
c1 = Checkbutton(root, text="Male", variable=checkvar1,
                 onvalue="Male is checked", offvalue="Male is not checked")
c2 = Checkbutton(root, text="Female", variable=checkvar2,
                 onvalue="Female is checked", offvalue="Female is not checked")
c1.pack()
c1.deselect()
c2.pack()
c2.deselect()
label1 = Label(root, textvariable=checkvar1).pack()
label2 = Label(root, textvariable=checkvar2).pack()
root.mainloop()

# Here is an example using radio buttons.
from Tkinter import *
root = Tk()
root.title("Radiobutton Test")
selection = StringVar()
selection.set("Nothing is selected")
r1 = Radiobutton(root, text="Diabetes", variable=selection,
                 value="Diabetes").pack()
r2 = Radiobutton(root, text="Hypertension", variable=selection,
                 value="Hypertension").pack()
r3 = Radiobutton(root, text="Depression", variable=selection,
                 value="Depression").pack()
label = Label(root, textvariable=selection).pack()
root.mainloop()

# Here is an example using an OptionMenu (i.e., a drop-down list).
from Tkinter import *
root = Tk()
root.title("OptionMenu Test")
selection = StringVar()
selection.set("Please make a selection")
options = ["Diabetes", "Hypertension", "Depression", "Alzheimer's disease",
           "Dementia", "Congestive heart failure", "Influenza"]
om = OptionMenu(root, selection, *options).pack()
label = Label(root, textvariable=selection).pack()
root.mainloop()

# Here is an example of packing, using the default packing style.
from Tkinter import *
root = Tk()
root.title("Packing Test 1")
label1 = Label(root, text="Red", bg="red", fg="white").pack()
label2 = Label(root, text="Green", bg="green", fg="black").pack()
label3 = Label(root, text="Blue", bg="blue", fg="white").pack()
root.mainloop()

# Here is the same widget set, using leftmost packing.
from Tkinter import *
root = Tk()
root.title("Packing Test 2")
label1 = Label(root, text="Red", bg="red", fg="white").pack(side="left")
label2 = Label(root, text="Green", bg="green", fg="black").pack(side="left")
label3 = Label(root, text="Blue", bg="blue", fg="white").pack(side="left")
root.mainloop()

# Here is a slightly longer example putting together many of the
# GUI concepts we've been talking about. We can graphically
# specify a query against a database of patients and their medical
# problems, represented by ICD-9 codes. By specifying a
# particular disease and (optionally) the sex of the patients we
# want to find, we can click a button and have a text file created,
# containing a list of resnums of all the patients matching our
# criteria. Note that the layout isn't very good. Later, we
# will work on this, using the grid() style of widget layout.
#
# Note: Those of you who have had my database or analytics courses
# will already know about this data, taken from the National Nursing Home
# Survey (NNHS). The data we are using here is not the medications data,
# but rather the morbidity data for the nursing home patients. The file
# "nnhs.sqlite3" should be available on the main page, right next to this
# snippets file. The "sqlite3" library, which comes with Python, allows
# programmers to interact with a relational database in the SQLite format,
# and use real SQL (Structured Query Language) queries. If you want more
# information on SQLite or the NNHS data, just let me know. Otherwise,
# you can just approach this as an example application.
from Tkinter import *
import sqlite3

diseases = {"Diabetes": "250", "Hypertension": "401.9", "Depression": "311",
                "Alzheimer's disease": "331.0", "Dementia": "294.8",
                "Congestive heart failure": "428.0", "Influenza": "487"}

def run_query():
    conn = sqlite3.connect("nnhs.sqlite3")
    cursor = conn.cursor()
    filestring = "patients_" + selection.get().lower()
    query = "SELECT DISTINCT patients.resnum from patients, icd9 "
    query += "WHERE patients.resnum = icd9.resnum "
    query += "AND icd9.code LIKE '" + diseases[selection.get()] + "%'"
    if (male.get() == True) and (female.get() == False):
        query += " AND patients.sex = 1"
        filestring += "_male"
    elif (male.get () == False) and (female.get() == True):
        query += " AND patients.sex = 2"
        filestring += "_female"
    query += ";"
    filestring += ".txt"
    outfile = open(filestring, "w")
    print(query) # Prints to the screen, not to the file!
    result = cursor.execute(query)
    for row in result:
        outfile.write(str(row[0]) + "\n")
    conn.close()
    outfile.close()

root = Tk()
root.title("Simple Query GUI")
sex_line = Label(root, text="Restrict to: ").pack()
male = BooleanVar()
female = BooleanVar()
male_button = Checkbutton(root, text="Males", variable=male,
                 onvalue=1, offvalue=0).pack()
female_button = Checkbutton(root, text="Females", variable=female,
                 onvalue=1, offvalue=0).pack()
disease_line = Label(root, text="Disease: ").pack()
selection = StringVar()
selection.set("Please make a selection")
om = OptionMenu(root, selection, *diseases.keys()).pack()
submit_button = Button(root, text="Run Query", command=run_query).pack()
quit_button = Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()
