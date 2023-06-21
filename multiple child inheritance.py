class father:
    def display(self):
        print("this is father")
class mother:
    def show(self):
        print("this is mother")
class child(father,mother):
    def disp(self):
        print("this is child")
c=child()
c.display()
c.show()
c.disp()                        
