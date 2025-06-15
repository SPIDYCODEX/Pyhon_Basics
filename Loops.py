# while Loop
i=1
while (i<5):
    print("hello")
    i+=1

name=[4,"rohit","bikash","roshan",2.4,False,True]
a=0
while(a<len(name)):
      print(name[a])
      a+=1

# For loop is using for iterate each value in list. it gives all the value on the list, tuple , dict, etc sequently.
for t in range(4):     #range function
     print(t)
b=[2,3,5,6,6,"rohit","bike",44/44,44.0]
for c in b:
    print(c)
x="spidy Developer🕷"
for z in x:
     print(z)
    #  Break & Continue\
for T in range(40):
    if(T==20):
        break     #it will print until 20 is come over :
    print(T)
for R in range(35):
    if(R==29):
        continue    # it will skip an iteration of the number which is choosen:
    print(R)
for I in range(44):
     pass

# Practice Questions
N=int(input("enter your num:"))
for i in range(11):
    print(f" {i} X {N}: {i *N}")
Name=["Rahul","Tulsi","Robin","Nikhi","Ritu"]
for n in Name:
   if(n.startswith("R")):
     print(f"Name is {n}")

n=int(input("enter your n"))   #multiplication using while loop
m=1
while(m<=10):
    print(f" {n} X {m} : {n * m}")
    m+=1

x=int(input("Enter a num:"))
for i in range( x):
    if x%i==0:
        print("the num is not prime")
else:
    print("The num is prime")
    
n= int (input("enter num:"))
product=1
for  i in range(1,n+1):
    product*=i
print(f"the factorial of {n} is {product}")
      
n=int (input("Enter num:"))
a=1
sum=0
while(a<=n):
    sum+=a
    a+=1
print(f"the sum of the natural num is {sum}")
a=int(input("enter Num:"))
for i in range(1,a+1):
    print(" " * (a-i), end="")
    print("*"*(2*i-1),end="")
    print(" ")
w=int(input("Enter your Num:"))
for x in range(1,w+1):
    print(" "*(w-x), end="")
    print("*"* x,end="")
    print(" ")
n=int(input("enter num:"))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2), end="")
        print("*",end="")
    print("")
