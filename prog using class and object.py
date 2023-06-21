#wap  using classes and objects to take the employess name and salary as input and calculate the total
#salary after deducing 0.2% from it
class employee:
    def __init__(self,n,s):
        self.name=n
        self.salary=s
    def change__data(self):
        return self.salary-0.002*self.salary
n=input("enter the name")
s=float(input("enter the salary"))
e=employee(n,s)
print(e.change__data())

           
        






