class student:
    print("This is student class")
    def __init__(self,age,name):
        self.age=age
        print("hello")
        self.name = name 




s1 = student(21,"aom")
s2 = student(21,"aom")  #This tells when ever an object is created only init method is called , while when a class is created all content outside function is being called..



#built in class attributes :- This are some of the class function which helps us to access, deleted and edit a variable


print(getattr(s1,"age"))
setattr(s1,"age",29)


print(getattr(s1,"age"))
print(hasattr(s1,"age"))
print(delattr(s1,"age"))
print(hasattr(s1,"age"))
print(s1)

print(s1.__dict__)

print(s1.__doc__)
z="aomkapadia"
print(z)
print(z.__doc__)
print(s1.__dict__)


print(student.__name__)

print(s1.__module__)
print(student.__module__)