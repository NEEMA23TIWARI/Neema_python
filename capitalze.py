'''s="hello world"
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())
print(s.isdigit())
print(s.isalpha())   #used to check whether string contains only alphabet
print(s.isalnum())   #to check whether or string is alpha numeric'''


#wap to input a string and count the number of letters,digits,and special characters in a string
m="helloABC123%$"
num1=num2=num3=0
for i in m:
    if i.isalpha():
        num1=num1+1
    elif i.isdigit():
        num2=num2+1
    else:
        num3=num3+1
print(num1,num2,num3)            


