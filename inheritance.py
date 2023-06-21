class employee:                  #parent class
    def __init__(self):
        self.salary=15000

class programmer(employee):           #child class
    def __init__(self):
        super().__init__()         #calling parent class constructor
    def give_bonus(self):
        return self.salary+1000
p=programmer()
print(p.give_bonus())            
        