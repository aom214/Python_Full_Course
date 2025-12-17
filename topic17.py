#partial function in python:--

#partial function basically helps us to create a new function from the old function where certain number iof arguments are fixed


from functools import partial


def add(a,b,c,d):
    return a+b+c+d 


g=partial(add,2,3)

print(g(1,2))




