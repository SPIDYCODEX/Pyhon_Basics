class school:
    name="rohit"   # These call class attribute
    age=20
    classes="9th"
govt= school()
# govt.skils
print(govt.name,govt.age,govt.classes)
private=school()
private.name="Udit"   # this is an Instance Attribute : instance attribute first comes over class attribute 
print(private.classes,private.age,private.name)

class roko:
    nickname="spidy"
    age=20
    skill="python"                  #Fuctions are use in OOPs when a self paramiter is pass on it

    def info(self):
         print(f"{self.nickname} starting to learn new skill:{self.skill}")

    @staticmethod   # Static method gives the output without use self parameter in OOPS while using function in it:
    def greet():
        print("HEllO CODER GOOD MORNING:")
Name=roko()
Name.nickname="SPidycoder🕷"
Name.greet()
Name.info()

class variable:
    name="stuart"
    age=23
    def __init__(self):   # It is called Dunder Method because it is called automatically:
        print("HellO i am a wild card enter in every programm☠")
var=variable()
print(var.name,var.age)

class roko:
    name="rohit"
    rage=36
rohitKohli=roko()
rohitKohli.name="kohli"
print(roko.rage)
print(rohitKohli.name)
print(roko.name)
class visual:
    name="vs"
    work="code"
    @staticmethod
    def info():
        print(visual.name,visual.work)
v=visual()
v.info()
class variable:
    mention="motorola"
    app="microsoft"
    salary=120000
    def __init__(self,name,grade,mention,app,salary):
        print("Hello i am introducing Self constructor")
        self.app=app
        self.salary=salary
        self.name=name
        self.mention=mention
        self.grade=grade
        
var=variable("rohit","A+","realme","google",1400000)
print(var.name,var.mention,var.salary,var.grade)

class programmer:
    company="google"
    def __init__(self,name,age,salary, pincode):
        self.name=name
        self.age=age
        self.salary= salary
        self.pincode=pincode
pro=programmer("Udit","age=twenty",1400000,765033)
p=programmer("rohan",22,1500000,89080)
print(pro.name,pro.age,pro.salary,pro.company)
print(p.name,p.age,p.salary,p.pincode)

class calculator:
    n=int (input("ENter n:"))
    def square(self):
        print(f'the sqare of {self.n} is : {self.n*self.n}')
    def cube(self):
        print(f'the cube of {self.n} is : {self.n*self.n*self.n}')

calc=calculator()
calc.square()
calc.cube()
class calc:
    # a=int(input("Enter a:"))
    def __init__(self):
        n=int(input("enter n:"))
        self.n=n
        print(f'the sqareroot of {n} is : {n**1/2}')
c=calc()


class a:
 @staticmethod
 def b():
    n=int(input("enter n:"))
    m=int(input("Enter m:"))
    print(f'the division of {n} - {m} = {n-m}')
c=a()
c.b()
class b():
 


    


