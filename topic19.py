#Vraiable:- A variable is basically a container which staore some data and data can be in any format it can be in form of string , tuple , dict ,list etc

# Class Vraiables:-- Class variables are bascially the variables which are defined inside a clas

#1. Instance Variable:- Instance variables are basically the variable which are specific for a particular object or the instance of a class.

# For exmaple:-

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age 
        print("This age:- "+str(age)+" and name:- "+name+" are instance variable of the class Student.")


s1=Student("aom",20)



#2. Class Variables:- Class variables are basically the variables which are made for the entire class and are distributed to all the objects.



class Person:
    college = "Ahmedabad University"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def instance_method(self):
        print(self.name)
    @classmethod
    def class_method(clss):
        clss.college="AHMEDABAD"
        print(clss.college)

p1=Person("aom",20)


#This class variable can only be change by using the class itself and it will reflect in all the object

Person.college = "AU"

print(Person.college)    # By only this way we can change class variable of a class




# Instance Method :-  Instance Method is basically a method which belongs to a particular instance of a class or object It can access instance variables as well as class variables.



p1.instance_method()


Person.class_method()
p1.class_method()


# Getter and setter Method:- In python By default we dont have getter and seeter method we dfeine them on our own to accessa nd modify the private variables


# private Variable:- private variables are basically the variables which can be only access and modify by using the method.
# in python we can create them by using __ in front.

class get:
    __pri="college"
    def __init__(self,name,age):
        self.__name=name    
        self.age = age 
    def access(cls):
        print(cls.__pri+cls.__name)

    @staticmethod
    def z1():
        print("hello World")
g1=get("aom",21)
g1.access()

g1.z1()


        


