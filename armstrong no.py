num=int(input("Enter the number"))
s=0
temp=num
while(temp!=0):

    a=temp%10
    b=pow(a,3)
    s+=b
    temp=temp//10
if(s==num):
    print("Armstong number")
else:
    print("not an armstrong no")
    