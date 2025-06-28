f=open("File.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()
#  READ FILE:
f=open("File.txt")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
f.close()
# WRITE FILE:
f=open("File.txt","w")
data=f.write("HELLO i am learning python \n i want to be a ai/ml developer:")
print(data)
f.close()
f=open("rohit.txt","w")
f.write("Hi")   #It creats a new file while the file doesn't exist in the folder before:
f.close()
f=open("ROko.py",'a') 

a=f.write("Hello python")
print(a)
f.close()

with open("File.txt") as f:
    print(f.read())
# with open("File.txt") as f:
#     (f.write("Twinkle Twinkle Little star\n what is happening here yaar."))
    # print(f.read())
    if "Twinkle" in "File.txt":
        print("Twinkle in the file exist:")
    else:
        print("Twinkle is not found in the file")
f=open("QNA_rw","a")
f.write("Then i will learn data science")
# f.read()
f.close()
f=open("QNA_rw","r+")   # r+ helps to read and write the file. after read it will overwrite the file 
f.write("I am learning Python right now")
print(f.read())
f.close() 
with open("app.txt","a+") as f:
    f.write("HEllo moto:")
    print(f.read())
import os 
os.remove("app.txt")  # It wil/l help to remove the file :


Practice Questions: 
with open("practice.txt","w+") as f:
    f.write("Hi everyone\n i am learning FIle I/O\n using Java.")
    f.write("\ni like to do DSA thorugh it")
    data=f.read()
    print(type(data))
    data.replace("java","Python")
print(data)

with open("practice.txt") as f:
    data =f.read()
    print(data)
    a=data.replace("Java","Python")
    print(a)
    print(a.split())
def tablegenerate(n):
    table=""
    for i in range(1,11):
        table+=f"{i} X {n}={i*n}\n"
    with open(f"tables/table{n}.txt","w") as f:
        f.write(table)
for i in range(2,11):
    tablegenerate(i)
 