# HINF 5502 - Assignment 4
# Shell of a program to validate ICD-10 codes
import re


# Put your regular expression pattern into the empty quotes below, and
# test your pattern by running the program. Remember to put the associated
# text file in the same directory as this program. Note that the columns in
# the output may not always line up. While this can be fixed, we did not
# discuss formatted output in this course, so we will not confuse everyone
# by using it here. It should be easy enough to read, in any case. If you
# want to see it with all the columns lined up properly, try opening it in
# a spreadsheet program such as Microsoft Excel.


# Enter Your Pattern Here
pattern = "^([A-Z][0-9]{2})$|^(([A-Z][0-9]{2})(\.)([0-9]{1,3}))$"


#  Process codes file
print("\npattern='{}'\n".format(pattern))
regexp = re.compile(pattern)
infile = open("HINF5502_Assignment_4_Codes.txt", "r")
infile.readline()
print("CODE\t\tTRUE STATUS\tCALCULATED\tRESULT")
errors = 0
for line in infile:
    line = line.strip()
    elements = line.split("\t")
    outstring = elements[0] + "\t\t" + elements[1] + "\t\t"
    if regexp.search(elements[0]):
        re_status = "Valid"
    else:
        re_status = "Invalid"
    if elements[1] != re_status:
        matched = "mismatch"
        errors += 1
    else:
        matched = "ok"
    print("{:15s} {:15s} {:15s} {}".format(elements[0], elements[1], re_status, matched))
infile.close()
print("\nErrors detected: {}\n".format(errors))
