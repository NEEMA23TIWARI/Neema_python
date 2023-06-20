#recursion
#wap to calculate factorial of anum using recursion

def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter any value"))
fact=factorial(num) 
print(fact)   