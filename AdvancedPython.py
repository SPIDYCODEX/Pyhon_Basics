# #Exception Handling in Python:
try:
 a=int(input("Enter a:"))
 print(a)
except Exception as e: # It is Not Give Error while You enter input str value instead of Integer value:
 print(e)
 print("There is Error for Getting Str value in input:")

#  Raising  Exceptions:

a=int(input("Enter Num1"))
b=int(input("Enter Num2"))
if b==0:   # It gives error when we try to devide by 0:(ZeroDivisionError)
    raise ZeroDivisionError("Programm doesn't run by divide with 0")
else:
 print(f"the division of the numbers is{a/b}")

#  try_else in python:
try:
    a=int(input("enter a:"))
    print(a)

except Exception as e:
    print(e)
else:   # Else Run when try successfully run : otherwise it isn't give output
    print("heyy there i am inside Else:")
   
try:
    a=int(input("enter a:"))
    print(a)

except Exception as e:
    print(e)
finally:   # It runs even the error executed 
    print("heyy there i am inside Finally:")
   
   # Global Keyword;

a=44
def fun():
        global a
        a=4 # it makes both variables input same:
        print(a)
fun()
print(a)
#  Enumerate function: Gives both index and item
List=[1,2,3,4,5,6]
for index,i in enumerate(List):
        print(f'the index {index} number value is :{i}')

# List Comprehensions:
L=[33,53,34,35,54]
sumlist=[i+i for i in L] # It gives the sum of the iteration+iterartion value with itself
print(sumlist)
print(sum(L))  # it gives the total of sum of the list 

# Lambda Funtion:
def square(n):
    print(n*n)
square(5) #instead of this writing function we can assume in lambda function:

Square=lambda n: n*n
print(f"the square of the Number is {Square(4)}")
sum=lambda a,b,c:a+b+c
print(f"the sum of the number is : {sum(4,5,6)}")


# Join methods / Bin methods:(Only for Strings)
lists=["apple","microsoft","Amazon","delloite"]
j="::".join(lists)
print(j)

      
# Map, Filters and Reduce:
# Map helps to applies all the items in a input list function:
n=[2,4,5,6]
Sqr=lambda x:x*x
maping=map(Sqr,n)
print(list(maping)) # we have to convert the variable into list , because map is only apply on a input list:  

#Filter example:
def even (n):
    if n%2==0:
        return True
    return False
EvenNo=filter(even,n) # it will helps to filter the function which we input there:
print(list(EvenNo))

#Reduce example:
def sum(a,b):
    return a+b





