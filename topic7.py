# Scope:- It refers to the region where a variable or function can be accessible..
#for example:-


# is_all(10,20) name 'is_all' is not defined..


def is_all(a,b):
    print(a+b)
a=10
print(a) # This is its scope here the variable with name a is accessible 

# Varibale :- It is basically a conatiner which conatins some value..

#Identifier:- It is basically a name given to something like variable , function , class, etc


#Types of identifies:--

# Local Identifier:--

def is_add(num):
    n=10
    print(num,n) #here num and n are local identifiers we can only used them inside function.

is_add(10)
# print(num,n) we cannot able to print them here as they are only locally accesible in function



# types of scopes:--

#Local Scope:-

#The variable which are defined inside a function can be accessible only inside that function.



# The local scope is automatically creted whenevr the function is being called and variable are assigned in that particular scope and their values are given whever the function stops running this local scopes disappers and variables are being removed from the memory, so to keep variables isolated and also to make code safe.




x=100
def is_local_function(q,b):
    x=10
    print(locals())
    print("Global inside Funcion")
    print("-"*50)
    print("globals:--",globals())  # this baisally gives all local variables 


print("-"*50)

is_local_function(10,20)
print("-"*50)
print("local outside function")
print(locals())

print("-"*50)
print("global outside function")
print(globals())