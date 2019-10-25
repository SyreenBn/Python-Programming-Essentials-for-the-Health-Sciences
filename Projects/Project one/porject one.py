file_object = open("icd10cm.txt","r")
ill = input(': ')
count = 0
for line in file_object:
        line = line.strip()
        elements = line.split("\t")
        if ill == elements[0] or ill.upper() == elements[0] :
           print (elements[1])
        elif ill == elements[1] :
           print (elements[0])
        else :
           common = elements[1].split(" ")
           i = 0
           
           for word in common:
              if common[i].lower() == ill.lower(): 
                 print (elements[0])
                 count = count + 1
                 break
              i = i + 1
file_object.close()
