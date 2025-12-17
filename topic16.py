#Decorator in python:--

#Decorators basially helps us to add additional functionality to a fucntion without modifying it..


def additional(func):
    def inner(z):
        print("This is additional functionality added to this function")
        func(z)
    return inner 
@additional
def main_func(s):
    print(s)



# this decorato0r is same as we use z=additional(main_fucn), z("hello")

main_func("hello")



# multiple decorator in python:--


def decor1(name):
    def name_upper():
        z = name()
        print("decor1")
        return z.upper()
    return name_upper
def decor2(uppe):
    def name_split():
        z=uppe()
        print("decor2")
        return z.split(" ")
    return name_split


@decor2
@decor1
def name():
    name = str(input())
    return name

print(name())




# problem statement1 make a decor function which return if there is an error or not without using try catch


def decor(func):
    def wrapper(*args):
        for i in range(1,len(args)):
            if args[i]==0:
                return "cannot divide by zero error"
        return func(*args)
    return wrapper 
@decor
def divisor1(a,b):
    return a/b

@decor
def divisor2(a,b,c):
    return a/b/c

print(divisor1(10,0))
print(divisor2(10,1,0))