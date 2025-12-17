# Multiple Inheritance:- child inheriting from multiple parent class.


class country:
    def __init__(self,office):
        self.office=office 
        print("Office:- ",office)

class district:
    def __init__(self,office):
        self.office = office 
        print("office2:- ",office)


class child(district,country):
    pass 

c1 = child("Ahmedabad")

# The choosing of method if the methods names are same in both inheiting class then it will be based on the order which we ahve user..

print(c1.__dict__)


print(child.mro())

def s(a,b):
    return a+b 

def s(*args):
    print(args)
    return sum(args)

print(s(10,20)+s(10,20,30))