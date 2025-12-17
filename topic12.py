# First Class Object In Python:--

print(type([]))


# First class object are basically the objects which we can use as any other value , we can able to assign a variable to it , pass them as an argument to other function, return them from function or can be able to store in any data structure .



# same for first class function :- It helps us to create decorators , closures  and implement callbacks..


# for example 

def getname():
    first_name = str(input("enter your first name"))
    last_name = str(input("Enter your last name"))
    return first_name+" "+last_name

def Display(func):
    return func()
    pass 

print(Display(getname))



# Higher order function:--

# Higher order function are the function which takes another fucntion as an input or return another function as an output



# map , reduce and filter are higher order function 

