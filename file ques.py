#wap to read all vowels from a text file
'''file=open("D:\\neema.txt","r")
for i in file.read():
    if(i=="a" or i=="e" or i=="i"or i=="o" or i=="u"):
        print(i)
file.close() '''   
 

#wap to print only those lines from the file which starts with 'A'
file=open("D:\\neema.txt","r")
for i in file.readlines():
    if(i[0]=='A'):
        print(i)
file.close()


#wap to write a list to a file
#wap to copy the contents of a file in another file
#Wap to extract characters from various text files and put them in a list


