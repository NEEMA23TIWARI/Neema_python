'''file=open("D:\\neema.txt")
print(file.tell())         #it gives file pointer current location
file.seek(10)              #it changes file pointer location 
print(file.read())
print(file.tell())'''

#another method to read
with open("D:\\neema.txt","r") as f:
    print(f.read())
