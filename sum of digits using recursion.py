#calculate sum of digits using recursion
def demo(num):
    if(num==0):
        return 0
    else:
        return num%10+demo(num//10)
print(demo(153))    


