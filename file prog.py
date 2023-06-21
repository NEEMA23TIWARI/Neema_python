#wap to input names and marks of 3 students and write it into a file
#john 78
#amit 67   
#pooja 55

'''file=open("C:\\Users\\neema\\Downloads\\text.txt","w")
for i in range(3):
    name=input("enter the name")
    marks=int(input("enter age"))
    file.write(name+" "+str(marks)+"\n")
file.close()'''


'''file=open("C:\\Users\\neema\\Downloads\\text.txt","a")  #append is used to add new data
for i in range(3):                                      #but it shows the previous data also
    name=input("enter the name")
    marks=int(input("enter age"))
    file.write(name+" "+str(marks)+"\n")
file.close()'''


#to delete a file
import os
os.remove("C:\\Users\\neema\\Downloads\\text.txt")