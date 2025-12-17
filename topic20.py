#Inheritance:- It means deriving a new class from the exisiting class in such a way that derived class can access all attributes and methods of parent class


class person:
    h1="person1"
    def __init__(self,name):
        self.name=name 

class manager(person):
    # def __init__(self,age,name):
    #     self.name=name
    #     self.age=age
    #     print(self.h1)
    def hello(self):
        print(self.h1)
        print(self.name)


p1=manager("aom")

print(p1.name)


p1.hello()