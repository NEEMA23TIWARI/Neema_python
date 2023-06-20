#wap to create a function which should accept two parameters as input and swap them and print updated vaslues
'''def swap (x,y):
    temp=x
    x=y
    y=temp
    print(x,y)
a=input("enter any no")
b=input("enter the value")
swap(a,b)'''

#or
def demo(a,b):
    a,b=b,a
    print(a,b)
p=input("enter value")
q=input("enter value")
demo(p,q)  