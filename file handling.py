'''file=open("C:\\Users\\neema\\Downloads\\text.txt")          #location of file and name of file
if(file):
    print("exists")
else:
    print("does not exist") '''     #to check whether file exist or not

#to read data from file
#print(file.read(10))                 #read the data of specified number of bytes
#print(file.readline())                 #it reads only a single line from file
#print(file.readlines())                 #it reads every line in form of list
               #if we put readline multiple times than it will start reading from next line


'''for i in file.readlines():           #loop can also be used to read data from a file 
    print(i)   '''


#write a data to a file
file=open("C:\\Users\\neema\\Downloads\\text.txt","w")
file.write("i am learning python")
file.close



