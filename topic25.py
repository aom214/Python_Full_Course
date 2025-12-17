#class decorartors:- They are basically the decorator which helps you to add some additional functionality to a function without modifying it by using class



class Decorator:
    def __init__(self,func):
        self.func = func 
    def __call__(self,a,b):
        result = self.func(a,b)
        return result**2 


@Decorator
def add(a,b):
    return a+b 

print(add(5,10))


#for example here we add an additional functionality to a add fucntion which return the square of its output....



def Decorator2(func):
    def wrapper(a,b,c):
        result = func(a,b)
        return func(result,c)
    return wrapper 

@Decorator2
def addition(a,b):
    return a+b 



print(addition(10,20,30))   #same as this 
                                                # c1 = Decorator2(addition)

                                                # print(c1(10,20,30))


class Decorator3:
    def __init__(self,func):
        self.func = func 
    def __call__(self,*args):
        s=0
        for num in args:
            s+=self.func(int(num))
        return s



@Decorator3
def add(*args):
    sum=0
    for num in args:
        sum+=num 
    return sum 


print(add(1,2,3,4,'5',6))




# property built in decorator use in python:--



class employee:
    def __init__(self,name,age):
        self._name = name 
        self.age = age 
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,ema):
        self._name=ema

e1 = employee("aom",21)
e1.name="aom123456"
print(e1.name)




class int:
    pass 

def hello():
    pass

print(callable(hello))




class a:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 



print(a.__call__)