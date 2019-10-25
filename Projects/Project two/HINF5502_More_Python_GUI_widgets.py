# HINF 5502: Program snippets: More Python GUI widgets
#
# Here are some short(ish) program snippets on Graphic User Interfaces (GUIs).
# For best results, be sure to run each of them in their own
# window as a program, rather than typing them in one line at a
# time in IDLE's shell.
#

# A simple interface, using the grid() manager for layout. We'll place
# two labels next to two single-line text entry fields. Note that the
# program really doesn't *do* anything, other than display the fields.
# Row and column coordinates default to "0" if not specified, but note
# that I am writing them out explicitly here. (It's often good practice!)
from Tkinter import *
root = Tk()
label1 = Label(root, text="Medical Record Number").grid(row=0, column=0)
label2 = Label(root, text="Date of Visit").grid(row=1, column=0)
e1 = Entry(root).grid(row=0, column=1)
e2 = Entry(root).grid(row=1, column=1)
root.mainloop()

# Let's do a few extra things to make the interface look a little better.
from Tkinter import *
root = Tk()
root.config(background="grey")
root.title("EHR Search")
label1 = Label(root, background="grey", justify="right", text="Medical Record Number:").grid(row=0, column=0, sticky=E)
label2 = Label(root, background="grey", justify="right", text="Date of visit:").grid(row=1, column=0, sticky=E)
e1 = Entry(root).grid(row=0, column=1)
e2 = Entry(root).grid(row=1, column=1)
root.mainloop()

# Now, let's actually do something with what's typed into a text field.
# This program will echo what's typed in when the "Submit" button
# is pressed. There is also a "Reset" button that will clear the field.
# Note that we're using StringVar objects to hold the text data. When we
# perform operations on them, any widgets that depend on what they contain
# are automatically changed.
from Tkinter import *
root = Tk()
root.title("Text Entry Updating Demo")
mrn = StringVar()
mrn_copy = StringVar()
label1 = Label(root, text="Medical Record Number:", justify="right").grid(row=0, column=0)
e1 = Entry(root, textvariable=mrn).grid(row=0, column=1)

def submit():
    mrn_copy.set(mrn.get())
def reset():
    mrn.set("")

submit_button = Button(root, text="Submit", command=submit).grid(row=1, column=0)
reset_button = Button(root, text="Reset", command=reset).grid(row=1, column=1)
label2 = Label(root, text="What was submitted:").grid(row=2, column=0)
label3 = Label(root, textvariable=mrn_copy).grid(row=2, column=1)
root.mainloop()

# This program will create a Text widget, which can hold user-editable text.
# Here, we allow the program itself to add text, in the form of a short file.
# Pressing the "Load file" button will add the text. Repeated presses will
# add more text to the end of what is already in the widget. Note that the
# contents of the field will scroll, but there are no explicit scrollbars.
# There are scrollbar widgets in Tkinter, but they are beyond our scope. See
# just about any Tkinter reference site on the web for instructions and examples
# on how to add and use scrollbars in widgets.
#
# In the load() function, the textfield.insert() command requires two things: where
# to put the text in the first argument, and what text to insert as the second. Here,
# it is END as the first argument, a special value that means "the end of whatever
# is already in the widget", and "line" is of course the line from the file that has
# just been read. The clear() function uses textfield.delete(), which takes "1.0"
# as the first argument, and stands for where to start removing text ("1.0" means
# "line 1, column 0"), and the special END value for the end of the text. Finally,
# when placing the Text widget in the grid layout, we are using "rowspan=2" to
# tell grid that while the widget "starts" in row 0, column 1, it will span two
# rows. Try taking the rowspan argument out, and noting what the window looks like.
# One of the buttons will move a bit. Can you see why?
from Tkinter import *

def load():
    infile = open("icd10_small.txt", "r")
    for line in infile:
        textfield.insert(END, line)

def clear():
    textfield.delete(1.0, END)

root = Tk()
root.title("File Viewer")
b1 = Button(root, text="Load File", command=load).grid(row=0, column=0)
b2 = Button(root, text="Clear", command=clear).grid(row=1, column=0)
textfield = Text(root)
textfield.grid(row=0, column=1, rowspan=2)
root.mainloop()

# Here's a demonstration of menus. We're creating top-level menus that will
# have an appropriate look to your system (Windows: in-window menus; Macintosh:
# menu bar menus at the top of the screen). We'll create "File", "Edit", and
# "Query" menus. The File and Edit menus will have dummy entries, while the
# Query menu will have entries that duplicate the functions of the two
# buttons we created in the above example.
from Tkinter import *
root = Tk()
root.title("Menu Demo")
mrn = StringVar()
mrn_copy = StringVar()
label1 = Label(root, text="Medical Record Number:", justify="right").grid(row=0, column=0)
e1 = Entry(root, textvariable=mrn).grid(row=0, column=1)

def submit():
    mrn_copy.set(mrn.get())
def reset():
    mrn.set("")
def hello():
    print("Hello!")

submit_button = Button(root, text="Submit", command=submit).grid(row=1, column=0)
reset_button = Button(root, text="Reset", command=reset).grid(row=1, column=1)
label2 = Label(root, text="What was submitted:").grid(row=2, column=0)
label3 = Label(root, textvariable=mrn_copy).grid(row=2, column=1)

menubar = Menu(root)
# Here's the File menu:
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hello)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
# Here's the Edit menu:
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)
# And finally the Query menu:
querymenu = Menu(menubar, tearoff=0)
querymenu.add_command(label="Submit Query", command=submit)
querymenu.add_command(label="Reset Text Field", command=reset)
menubar.add_cascade(label="Query", menu=querymenu)
# Lastly, display the whole thing (note that this isn't via grid() or pack()!
root.config(menu=menubar)
root.mainloop()

# Now we have the tools we need to improve the SQL query tool we built in
# Week 13. We can lay out the widgets a bit better, and can create menus.
# Unlike the Week 13 snippet, this program also orders the patient numbers!
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
        query += " AND patients.sex = 1 "
        filestring += "_male"
    elif (male.get () == False) and (female.get() == True):
        query += " AND patients.sex = 2 "
        filestring += "_female"
    query += "ORDER BY patients.resnum;"
    filestring += ".txt"
    outfile = open(filestring, "w")
    print(query) # Prints to the screen, not to the file!
    result = cursor.execute(query)
    for row in result:
        outfile.write(str(row[0]) + "\n")
    conn.close()
    outfile.close()

root = Tk()
root.title("Better Query GUI")
sex_line = Label(root, text="Restrict to:").grid(row=0, column=0, sticky=E)
male = BooleanVar()
female = BooleanVar()
male_button = Checkbutton(root, text="Males", variable=male,
                 onvalue=1, offvalue=0).grid(row=0, column=1, sticky=W)
female_button = Checkbutton(root, text="Females", variable=female,
                 onvalue=1, offvalue=0).grid(row=0, column=2, sticky=W)
disease_line = Label(root, text="Disease:").grid(row=1, column=0, sticky=E)
selection = StringVar()
selection.set("Please make a selection")
om = OptionMenu(root, selection, *diseases.keys()).grid(row=1, column=1, columnspan=2)
submit_button = Button(root, text="Run Query", command=run_query).grid(row=2, column=0)
quit_button = Button(root, text="Quit", command=root.destroy).grid(row=2, column=2, sticky=E)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)
querymenu = Menu(menubar, tearoff=0)
querymenu.add_command(label="Run Query", command=run_query)
menubar.add_cascade(label="Query", menu=querymenu)
root.config(menu=menubar)
root.mainloop()
