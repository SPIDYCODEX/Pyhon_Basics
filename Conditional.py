a=int(input('Enter Your 1st Num:'))
b=int(input('Enter Your 2nd Num:'))
c=int(input('Enter Your 3rd Num:'))
d=int(input('Enter Your 4th Num:'))
if (a>=b and a>=c and a>=d):                  #Qeustion of Find the Greatest Num of 4 :
    print("the Greatest Num is a :",a)
elif(b>=c and b>=d):
    print("The Greatest Num is b:",b)
elif(c>=d):
    print("The Greatest Num is c:",c)
else:
     print("The Greatest Num is d",d)

     #Qestion 2- Students Pass or Fail:

Phy=int(input("Enter Your  Phy Mark:"))
Chem=int(input("Enter Your chem Mark:"))
Math=int(input("Enter Your math Mark:"))
Marks=(  100 * ( Phy + Chem + Math )) /300
if (Marks >= 33):
    print("You are pass:", Marks)
else:
    print("You are Failed", Marks)
 
# Qestion 3 Character count 
Name= input("Enter Your Name:")
Len=len(Name)
if (Len<=10):
    print("IT is less than 10 character Name:",Name)
else:
    print("IT is a 10 or More than character Name:",Name)


# Qestion 4 Fixing the Grade of the students:
marks=int(input("Enter Your Marks:"))
if (marks >=90 and marks <100):
    Grade="A"
elif (marks >=80 and marks<90):
    Grade = "B"
elif(marks >=70 and marks< 80):
    Grade="C"
elif(marks >=60 and marks<70):
    Grade="D"
elif(marks >=50 and marks<60):
    Grade="E"
else:
    Grade= "F"
print("Your Grade is:",Grade)
          