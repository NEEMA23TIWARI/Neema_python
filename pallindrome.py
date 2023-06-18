num=int(input("Enter the number"))
temp=num
s=0
while(num!=0):
    a=num%10
    s=s*10+a
    num=num//10
if(temp==s):
    print("Palindrome")
else:
    print("Not palindrome")