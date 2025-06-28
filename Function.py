# # Fucntion is a group of statement perform in a specific task
def calander(name="virat"):
    print(f"{name} today is June 13: Friday")
calander("rohit")
calander()
def calculation(a,b,c):
   sum =a + b+ c
   print(sum)
   return sum
calculation(1,3,5)

Name=["mihir","akash","samir","kiran","sudha",4,44.5]
def list(a):
    print(len(a))
    print(a[3])
    
    return a
list(Name)
#factorial of a num
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(f"the factorial of the {i}is : {fact}")
factorial(5)
# convert USD value to INR
def converter(usd):
    INR=usd*83
    print(f'the usd value in INR is: {INR}')
    return INR
usd=int(input("Enter the num:"))
converter(usd)
# odd even check:
def Num(n):
    if (n%2==0):
        print(f"the Num is Even:{n}")
    else:
        print(f"the Num is Odd:{n}")
n=int(input("Enter the num:"))
Num(n)
# factorial calculation using recursion
def Number(n):
    if(n==1 or n==0):
        return 1
    return n*Number(n-1)
n=int(input("Enter the number:"))
print(f"the factorial of the {n} is: {Number(n)}")
print(Number(n))
# celsious  convert
def faranide(f):
    return 5*(f-32)/9 #or c=58*(f-32)/9
f=int(input("Enter the tem:"))
c=faranide(f)
print(round(c,2))

# sum of all natural numbers
# n= (n-1) +n
def sum(n):
   if n==1:
     return 1
   return sum(n-1)+n
n=int(input("Enter the num:"))
print(f"the sum of the {n} is {sum(n)}")
def star(n):
   for i in range(1,n+1):
      print("*"*i, end="")
      print("")
n=int(input("enter the num:"))
star(n)
def pattern(n):
   if(n==0):
      return 
   print("*"*n)
   pattern (n-1)
n=int(input("Enter the n:"))
pattern(n)
# inches to cm
def inch_to_cm(n):
   return n * 2.54
n=int(input("The Inch is:"))
print(f"the {n} inches is equal to {inch_to_cm(n)} cm")
inch_to_cm(n)
# multiplication of the number:
def num(n):
   a=1
   while(a<=10):
      print(f"{a} X {n} = {a * n}")
      a+=1
n=int(input("Enter the num "))
num(n)

 
def mothere():
   n=int(input("Enter n:"))
   if n==0 and n==1:
    return 0
   print(n*(n-1))
mothere()
def star():
    n=int(input("Enter No of Star:"))
    for i in range(n+1):
        print("*"*i,end="")
        print("")
star()
