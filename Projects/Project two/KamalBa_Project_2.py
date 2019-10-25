from Tkinter import *
root = Tk()
root.title("Project#2")
user_input = StringVar()
user_input_copy = StringVar()

label = Label(root, text="Please Enter a Code").grid(row=0, column=0)
inputVar = Entry(root, textvariable=user_input).grid(row=1, column=0)
def submit():
    import urllib.request, re
    infile = open("icd10cm.txt", "r")
    regexp = re.compile(user_input.get())
    for line in infile:
        line = line.strip()
        if regexp.search(line):
            user_input_copy.set(line)
    
def reset():
    user_input.set("")

Run = Button(root, text="Submit", command=submit).grid(row=2, column=0)
Clear = Button(root, text="Clear", command=reset).grid(row=2, column=1)

Entry = Label(root, text="Result:" + "( Code" + " + " + "Description )").grid(row=5, column=0)
Output = Message(root, textvariable=user_input_copy).grid(row=6, column=0)
Exit = Button(root, text="Quit", command=root.destroy).grid(row=7, column=0)
root.mainloop()
