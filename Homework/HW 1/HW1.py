#-------------------------
# The first Program
#-------------------------

h1 = input('Enter your hight in meters : ')
w1 = input('Enter your weight in kilograms : ')
BMI1 = float(w1) / ((float(h1)/100)**2)
output = "Your IBM is: "
print ("Your IBM is: " + str(round(BMI1, 1)))

#-------------------------
# The second Program
#-------------------------

def bmi_calculator( hight, weight ):
   BMI_value = float(weight) / ((float(hight)/100)**2)
   return BMI_value

h2 = input('Enter your hight in meters : ')
w2 = input('Enter your weight in kilograms : ')
BMI2 = bmi_calculator( h2, w2)
print ("Your IBM is: " + str(round(BMI2, 1)))


