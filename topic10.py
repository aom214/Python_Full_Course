#Types of arguments:--

# 1. Positional Argument:-

def student(name,age):
    print(f"student name is : {name} and his age is: {age}")
student("AOM",20)
student(20,"AOM")



#2. Key word arguments:--

student(age=20,name="AOM")



#3. default arguments:--

def student(name,data=[]):
    data.append(name)    # This is beacuse defult argumets in python are defined only once so they dont chaneg
    print(name,data)

student("AOM")
student("AOM",["Z"])
student("HARSH")


#4. Variable length arguments:--

# a. variable length positional arguments:--

def add_(*s):
    print(sum(s))

add_(1,2,3,4,5,6)


def z(a,b,c,*s):
    print(a,b,c,s)

# z(10,20,30,a=100,b=200,c=300)  # error multiple values for argument a


def a(*s1,a,b,c):
    print(s1,a,b,c)

# a(10,50,60,a=20,c=30)  # error b argument is missing 

a(a=10,b=20,c=30)   
a(100,2000,3000,a=10,b=20,c=30)  



def q(a,b,*c):
    print(a,b,c)
q(10,20,30)




#b variable length keywords arguments:--

def s(z,**k):
    print(z,k)


s(20,a=10,b=30)

s(a=10,b=20,z=30)   # this will works 


def isa(a,*s,c):
    print(a,s,c)

# isa(1,20,10)  #error 1 keyword c is missing 




