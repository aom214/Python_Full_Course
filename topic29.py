#pickling and unpickling in python:-- pickling in python basically means to convert python object into bytes steam so that tehy can be stored in files or can be send over the internet..


# for pickling and unpickling we have 4 types load 

import pickle


class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age 
    def display(self):
        print(f"name of the student is :- {self.name}\n roll no of student is :- {self.roll}\n age of student is :- {self.age}\n")

n = int(input("Enter no of students :- "))
f = open("data.txt","wb")
for i in range(n):
    name = input(f"enter student{n+1} name:- ")
    roll = input(f"enter student{n+1} roll:- ")
    age = input(f"enter student{n+1} age:- ")
    s1 = Student(name,roll,age)
    pickle.dump(s1,f)
f.close()




#here objects are stored inside file now I am retreving it you can reterive it from any where till you have file access there:-----


f=open("data.txt","rb")
while True:
    try:
        obj=pickle.load(f)
        print(obj)
        obj.display()
    except Exception as e:
        print(e)
        break 
f.close()
