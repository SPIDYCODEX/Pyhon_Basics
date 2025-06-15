Names=["Peter","Jane","Harry","Ned"]
print(Names)
print(type(Names))
Names.sort()
print(Names)                        #Lists are Mutable
Names.append("Bruce")
print(Names)
print(len(Names))
Names.insert(3,"Marry")
print(Names)
Names.remove("Peter")
print(Names)
print(Names.pop(2))
print(Names.reverse())


tup=(1,3,"roko",33.4,True)
print(type(tup))
tup1=()  #Empty Tuple
tup2=(1,)  #single Tuple
print(type(tup))                        #Tuples Are Immutable
print(type(tup2))
a= tup.count(1)
print(a)
b=tup.index("roko")
print(b)

#Practice Questions
Fruits=[]
f1=input("Enter 1st fruit:")
f2=input("Enter 2nd fruit:")
f3=input("Enter 3rd fruit:")
f4=input("Enter 4th fruit:")
f5=input("Enter 5th fruit:")
f6=input("Enter 6t fruit:")
f7=input("Enter 7th fruit:")
Fruits.append(f1)
Fruits.append(f2)
Fruits.append(f3)
Fruits.append(f4)
Fruits.append(f5)
Fruits.append(f6)
Fruits.append(f7)

print( "Your Fruits Name is:",Fruits)
# print(len(Fruits))
Students=[]

s1=int(input("Enter your mark:"))
s2=int(input("Enter your mark:"))
s3=int(input("Enter your mark:"))
s4=int(input("Enter your mark:"))
s5=int(input("Enter your mark:"))
s6=int(input("Enter your mark:"))
Students.append(s1)
Students.append(s2)
Students.append(s3)
Students.append(s4)
Students.append(s5)
Students.append(s6)
print(Students)
Students.sort()
print(Students)

 #Qestions 4 To print the sum of the list
List=[11,22,33,44,55]
print(sum(List))
 # Questions 5 : To count the 0 in tuple
Given=(7,0,8,0,0,0,9)
a=Given.count(0)
print(a)
