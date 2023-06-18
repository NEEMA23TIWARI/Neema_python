# to input a number and print the sum of its digits
a,s=0,0
num=int(input("Enter the number"))
while(num!=0):
    a=num%10
    s=s+a
    num=num//10
print(s)