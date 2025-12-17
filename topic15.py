# namespaces in python :--

a=50

b=50

c=100

print(id(a))  # id return the memory address of an object
print(id(b))
print(id(c))

print(dir()) # lista names of namespaces

print(globals()) # dic of global namespaces

a="a o mkapadia"

print(a.split("a"))


def outer():
    x=10
    def inner1():
        return x 
    x+=1
    def inner2():
        return x 
    return (inner1,inner2)
func1,func2 = outer()
print(func1())
print(func1())
print(func2())

