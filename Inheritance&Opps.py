class salary:
   salary=1200000
   def getSalary(self):
      print(f"heis getting {self.salary} LPA wow..")

class company:
    company="microsoft"
    Name ="Spidy Coder"
    def programme(self):
        print(f'{self.Name} is hired by {self.company} Company🙌')
class programmer(company,salary):   # Using parents class in childclass : child  class(programmer), company and salary are perents  class.
    Name="coderx"
    language="python"                  # Multiple Inheritance
    def programmer2(self):
     print(f'he is good at {self.language} ')

p=programmer()
p.programme()
# print(p.company)
p.programmer2()
p.getSalary()
s=salary()
# s.programme()
# s.programmer2()
s.getSalary()

# Constructor (Super Inheritance)
class india:
   pin=765033
   District="Rayagada"
   country="India"
   @classmethod  # Class methods helps to call the class attribute instead of instance attribute:
   def __init__(self):
      
      print(f'the pincode of my district {self.District}  Is:{self.pin}')
I=india()
I.pin=705022
I.District="Behrampur"
class america(india):
   def __init__(self,n):
      self.n=n
    #   print(f'{self.country} is the most advanced technology country in the world')
      print(f'whiel {self.n} is the greatest Hollywood in the world:')
a=america("America")

# Questions solve:
class vector:
  def __init__(self,i,j):
    self.i=i
    self.j=j
    print(f'the 2Dvector is 1{self.i} + 2{self.j}')
class threeDvector(vector):
  def __init__(self, i, j,k):
    super().__init__(i, j)
    self.k=k
    print(f"the 3Dvector is 1{self.i} + 2{self.j} + 3{self.k}")
T=threeDvector("i","j","k")


#Q2
class Vectors: 
    def __init__(self,i,j):
      self.i=i
      self.j=j
    def twovector(self):
       print(f"the 2DVecotr is :{self.i}i + {self.j}j")
class ThreeDvector(Vectors):
   def __init__(self, i, j,k):
      super().__init__(i, j)
      self.k=k
   def show(self):
      print(f'the 3Dvector is:{self.i}i + {self.j}j + {self.k}k')
a=Vectors(1,2)
b=ThreeDvector(2,3,4)
a.twovector()
b.show()

    


         
      
      
   
      
    

      
      

      




    
   