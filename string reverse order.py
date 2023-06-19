'''#wap tp input a list and print the list in reverse order using loops
lst=eval(input("enter the list elements"))
for i in range(len(lst)-1,-1,-1):
    print(lst[i])
#or print(lst[::-1])'''

#slicing
#using slicing, fetch elements strating from 4 till a
#lst=[1,2,"a",True,4]
lst=[1,2,"a",True,4]
print(lst[-1:-4:-1])


