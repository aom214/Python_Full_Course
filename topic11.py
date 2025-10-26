#Lambda Function in python:--

# Lambda function with sorted fucntion:--


L=[5,3,6,4,1,9,10]

P=[[2,3],[5,1,2,3,4,5],[10,12,1],[1,2],[2,4]]

print(sorted(L))

print(sorted(P,key = len))
print(sorted(P,key = lambda x:len(x)))


print(sorted(P,key = lambda x:(x[1],x[0])))




# Nested Lambda function in python:--

add = lambda x: lambda y: x+y

print(add(10))

f=add(10)
print(f(30))


print(lambda x:x)




z = lambda x:x**2 + x 
print(z(8))




# short hand if lese:---


print(10 if 10>=20 else 20)

# In lambda 

z=lambda x,y: x if x>=y else y 
print(z(10,20))




# lambda function in list compherension 
z=lambda i:i*i
L=[z(i) for i in range(10)]
print(L)
nums = [1,2,3,4,5,6]
s = lambda x:[i*i for i in x]
print(s(nums))


z= lambda x,y:x*y

s = lambda f: lambda x,y:f(x,y)

print(s(z)(100,20)) 


iife_function_in_python = (lambda x:x**2)(10)

print(iife_function_in_python)


