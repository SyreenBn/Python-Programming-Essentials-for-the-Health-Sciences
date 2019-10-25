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
   final_result = [hight, weight, round(BMI_value,1), classification]
   return final_result
      
h1 = input('Enter your hight in centimeters : ')
w1 = input('Enter your weight in kilograms : ')
BMI1 = bmi_calculator( h1, w1)
print ("A weight of " + str(BMI1[1]) + " kg and a height of " + str(BMI1[0]) + "cm represent a BMI of " + str(BMI1[2]) + ", which is classified as " + BMI1[3] + ".")

