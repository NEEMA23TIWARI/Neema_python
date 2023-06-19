#wap to print the names and age of 5 students where names are the keys and ages are values
d={}
for i in range(1,6):
    name=input("enter the name")
    age=int(input("enter age"))
    d[name]=age
print(d)            
