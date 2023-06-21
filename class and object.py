'''class Student:                  #student is name of class
    name="amit"                 #a single class has multiple objects
    marks=78
s1=Student()                     #s1 and s2 are objects
s2=Student()
print(s1.name,s1.marks)  
print(s2.name,s2.marks)  '''

'''class Student:
    def __init__(self):
        print("this is constructor")
s1=Student()
s2=Student()'''        

'''#purpose of self is to create variables
class Student:
    def __init__(self):
        self.name="john"
        self.age=25
s=Student()
print(s.name,s.age)        
s1=Student()
s2=Student()'''

#we can pass two or more arguments in constructor            

'''class Student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
s=Student("john",27)
print(s.name,s.age)        
s1=Student("ria",67)
print(s1.name,s1.age)
s2=Student("neha",78)
print(s2.name,s2.age)'''


class Student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def change__data(self,n):
        self.name=n
        return self.name
s=Student("john",27)
updated__name=s.change__data("alfred")
print(s.name,s.age)
s2=Student("amit",28)
print(s2.name,s2.age)
