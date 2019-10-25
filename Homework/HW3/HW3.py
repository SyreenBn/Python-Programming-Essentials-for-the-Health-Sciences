def bmi_calculator( hight, weight ):
   BMI_value = (float(weight) / ((float(hight)/100)**2))/10000
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
file_object = open("bmi.txt","r")
i = 1
file_output = open("output.txt","w")
for line in file_object:
    if i == 1 :
        i = i + 1
    else :
        line = line.strip()
        elements = line.split("\t")
        h1 = float(elements[0])
        w1 = float(elements[1])
        BMI1 = bmi_calculator( h1, w1)
        file_output.write("A weight of " + str(BMI1[1]) + " kg and a height of " + str(BMI1[0]) + "cm represent a BMI of " + str(BMI1[2]) + ", which is classified as " + BMI1[3] + "."+"\n")
file_object.close()
file_output.close()
