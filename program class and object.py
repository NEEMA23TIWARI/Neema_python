#write a python class which has two methods get_string and print_string.
#get_string accepts a string from user and print string print the string in upper case

class python:
    def get_string(self):
        self.s=input("enter the string")
    def print_string(self):
        print(self.s.upper())
p=python()
p.get_string()
p.print_string()            
