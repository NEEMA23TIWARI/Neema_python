#local and global variable 
'''def demo():
    a=2  #local variable
    print(a)
demo()
print(a)     #it can not be acessed here as it is accesed up till that block only '''   


#global variable
'''name="john"
def demo():
    a=2
    print(a)
demo()
print(name) '''   

def demo(*args):               #args is used to give multiple values
    print(*args)
demo(1,2,3,4,5,6,7,8)    


