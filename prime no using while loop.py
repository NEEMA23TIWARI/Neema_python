#WAP to check if a number is prime or not
num=int(input("Enter the number"))
i=1
c=0
while(i<=num):
    if(num%i==0):
        c=c+1
    i=i+1   
        
if(c==2):
    print("Prime no")
else:
    print("Not prime")