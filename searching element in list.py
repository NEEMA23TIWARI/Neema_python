#wap to search for an element in a list asking from user 
#if element found print found else print not found 

lst=[1,2,3,"hello"]
search=eval(input("enter the data to find"))
for i in lst:
    if search==i:
     print("element found")
     break
else:
   print("not found")    

