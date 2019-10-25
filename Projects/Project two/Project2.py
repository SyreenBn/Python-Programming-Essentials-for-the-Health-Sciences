from Tkinter import *
root = Tk()
root.title("BMI Calculator")
mrn1 = StringVar()
mrn2 = StringVar()

mrn_copy = StringVar()
mrn_copy.set("                \n                  \n                 \n                  \n")
label1 = Label(root, text="Enter your hight in centimeters :", justify="right").grid(row=0, column=0)
e1 = Entry(root, textvariable=mrn1).grid(row=0, column=1)

label_2 = Label(root, text="Enter your weight in kilograms :", justify="right").grid(row=1, column=0)
e2 = Entry(root, textvariable=mrn2).grid(row=1, column=1)

def bmi_calculator( hight, weight ):
   BMI_value = float(weight) / ((float(hight)/100)**2)
   if BMI_value < 18.5 :
      classification = "Underweight"
   elif 25.0 > BMI_value >= 18.5 :
      classification = "Healthy weight"
   elif 30.0 > BMI_value >= 25.0 :
      classification = "Overweight"
   else :
      classification = "Obese"
   final_result = "A weight of " + str(weight) + " kg \n and a height of " + str(hight) + " cm \n represent a BMI of " + str(round(BMI_value,1)) + ", \n which is classified as " + classification + "."
   return final_result

def submit():
    mrn_copy.set(bmi_calculator(mrn1.get(),mrn2.get()))

def reset():
    mrn1.set("")
    mrn2.set("")
    mrn_copy.set("                \n                  \n                 \n                  \n")


submit_button = Button(root, text="Submit", command=submit).grid(row=2, column=0)
reset_button = Button(root, text="Reset", command=reset).grid(row=2, column=1)
label2 = Label(root, text="What was submitted:").grid(row=3, column=0)
label3 = Label(root, textvariable=mrn_copy).grid(row=3, column=1)
root.mainloop()

