#Nested Class:- It basically means a class inside another class , we use it when there are class which does not exist without each other for eg a university can have multiple college but a college does not exist if university does not exist and another is dob class does not exist if student does not exist 



#example:--

class Student:
    def __init__(self,name,age,dob):
        self.name = name 
        self.age = age 
        self.dob = self.Dob(dob)
    def Dispaly(self):
        print(f"This is {self.name}")
        self.dob.Dispaly()
    class Dob:
        def __init__(self,dob):
            self.dob = dob 
        def Dispaly(self):
            print(f"Dob is {self.dob}")
s1 = Student("aom",21,"24th novermber 2004")


s1.Dispaly()
                