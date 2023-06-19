#wap to search for an element in a list ny asking from user 
#if element is found,print found along with position
lst=[1,2,"hello",3]
search=eval(input("enter the element to find"))
for i in range(0,len(lst)):
    if(search==lst[i]):
        print("element found at index",i)
        break
else:
        print("not found")
