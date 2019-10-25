# HINF 5502: Program snippets: GUIs
#
# Here are some short(ish) program snippets on Graphic User Interfaces (GUIs).
# For best results, be sure to run each of them in their own
# window as a program, rather than typing them in one line at a
# time in IDLE's interactive window.
#

# A very simple GUI program, with just a Quit button.
from Tkinter import *
root = Tk()
button = Button(root, text="Goodbye",
                command=root.destroy)
button.pack()
mainloop()

# An example of named parameters. Note that there are many
# options for styling the text label.
from Tkinter import *
root = Tk()
label = Label(root, text="Hello", background="white",
              foreground="red", font="Times 20",
              relief="groove", borderwidth=3)
label.pack()
mainloop()

# A slightly larger example, creating an interface which has
# two buttons. One increments a counter in the same window, and
# the other button quits the program.
from Tkinter import *
root = Tk()
count_label = Label(root, text="0")
count_label.pack()
count_value = 0

def increment_count():
    global count_value, count_label
    count_value += 1
    count_label.configure(text=str(count_value))

incr_button = Button(root, text="Increment", command=increment_count)
incr_button.pack()
quit_button = Button(root, text="Quit", command=root.destroy)
quit_button.pack()
mainloop()

# A different version of the above, using the IntVar mutable
# type, making the code a little more straightforward.
from Tkinter import *
root = Tk()
count_value = IntVar()
count_value.set(0)
count_label = Label(root, textvariable=count_value)
count_label.pack()

def increment_count():
    count_value.set(count_value.get() + 1)

incr_button = Button(root, text="Increment", command=increment_count)
incr_button.pack()
quit_button = Button(root, text="Quit", command=root.destroy)
quit_button.pack()
mainloop()
