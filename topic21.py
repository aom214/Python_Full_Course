#Super Method:- It bascially helps us to access the properties of the parent class inside the child class.
#It bascially gives a temporary object which conatins the refrence to the parent class.

class parent:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def greet(self):
        print("Hello:- ",self.name)


class child(parent):
    def __init__(self,school,name,age):
        super().__init__(name,age)
        self.school = school 
        super().greet()
    @staticmethod
    def greet():
        super().greet()
c1 = child("Kidz Are Us","aom",21)

c1.greet()
