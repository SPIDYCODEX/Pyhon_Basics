Name="rohit"
print(Name)
print(Name[0:4])
print("rohit".upper())
print(len(Name))  #Gives the Length of the String
print(type(Name))
print(Name.replace("r","M"))

STR="2345566777"
print(STR[0:10])   # It goes to starting index to index 10
print(STR.count("2")) # To count the number of presence 
print(STR.find("2"))   #To find the position of the Number
STR.count("5")
# TASK OF THE STRING 
Name=input("Enter Your Name to Say :")
print("Good After Noon :",Name)
print(f"WELCOME TO DEVELOP WORLD {Name}")

      # Question 2
Letter= 'Dear <Name>\nYou are selected \n <Date>'
print(Letter.replace("<Name>","Spidy").replace("<Date>","March 6"))
Given="There is lot of flowers for sale  and fruit as well."
print(Given.find("  "))      #To find the double space in Given and replace that with single space
print(Given.replace("  "," "))