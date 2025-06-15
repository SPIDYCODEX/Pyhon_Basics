# #DICTIONARY IN PYTHON🐍
Dicttionary={"rohit": 20,"virat":23,"jadeja":23,"ashwin":40,
             "bumrah":25,"List":[2,4,5]}
print(Dicttionary)
print(Dicttionary["rohit"])
print(Dicttionary.get("virat"))
print(Dicttionary.items())     #gives the keys and their values
print(Dicttionary.keys())      #gives the keys only
print(Dicttionary.values())    #gives the values of keys
print(Dicttionary.pop("bumrah"))
Dicttionary.update({'rohit': 44})  #update the value and add a new key-value in dictionary
print(Dicttionary)
Dicttionary.update({'hardik':33})
print(Dicttionary)
Dicttionary.update({0:0})
print(Dicttionary)
marks={}   #An Empty dictionary
print(Dicttionary,type(Dicttionary))


#   SETS IN PYTHON
sets={4,54,6,"code"}
print(sets,type(sets))
sets.add(55)
print(sets)
sets.remove(4)
print(sets)
set2={1,2,4,5,"Vs"}
print(set2.add(54))
print(sets.union(set2))
print(sets.intersection(set2))
print(sets)
print(set2)
print(sets - set2 )

# practice questions of sets and dictionary
Dictionary={"kam":"work","Neend":"sleep","jao":"go"}
word=input("Enter Your Word to Know the mean in English:")
print(Dictionary[word])
 #question from set
s=set()  #empty set
n1=int(input("Enter Your num:"))
s.add(n1)
n2=int(input("Enter Your num:"))
s.add(n2)
n3=int(input("Enter Your num:"))
s.add(n3)
n4=int(input("Enter Your num:"))
s.add(n4)
n5=int(input("Enter Your num:"))
s.add(n5)
n6=int(input("Enter Your num:"))
s.add(n6)
n7=int(input("Enter Your num:"))
s.add(n7)
n8=int(input("Enter Your num:"))
s.add(n8)
print(s)
 #lentgh of set
Set=set()
Set.add(20)
Set.add(20.0)
Set.add("20")
print(Set)
print(len(Set))
print(type(Set))
#question of dictionary
Dict={}
Name1=input("Enter Your name:")
Lang= input("Enter Your Language:")
Dict.update({Name1:Lang})
Name2=input("Enter Your name:")
Lang2=input("Enter Your lang:")
Dict.update({Name2:Lang2})
Name3=input("Enter Your name:")
Lang3=input("enter Your lang:")
Dict.update({Name3:Lang3})
Name4=input("Enter Your name:")
Lang4=input("enter your lang:")
Dict.update({Name4:Lang4})
print(Dict)
marks_dict = {}
x=int(input("Enter Your mark:"))
marks_dict.update({"rohit":x})
x=int(input("Enter your mark:"))
marks_dict.update({"mohit":x})
x=int(input("Enter your mark:"))
marks_dict.update({"sihit":x})
x=int (input("Enter your mark:"))
marks_dict.update({"lihit":x})
print(marks_dict)
Sum=(sum(marks_dict.values()))
Average=Sum/4
print(Average)
Dict= {"Rohit":44,"Rakesh":90,"Monali":45,"Sonali":66,"Rini":78}
Student=input("Enter YOur name :")
Dict.get(Student)
if Student in Dict:
    print(f"The mark of {Student} is {Dict[Student]}")
else:
     print("Student Not FOUnd")