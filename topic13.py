
from functools import reduce
#Filter Function in python:--


L=[1,2,3,4,5,6,7,8,9,10]


print(list(filter(lambda x:x%2==0,L)))

L=[num for num in range(10) if num%2==0]


z = lambda x,y:x if x>y else y
print(z(1,2))



L="mcdcmcaefc"
z= list(filter(lambda x:x in ["a","e","i","o","u"],L))
print("".join(list(z)))





# filter student having marsk greater than or equla to 80

students = {"aom":99,"harsh":100,"soham":95,"tathya":90,"ganshyam":40}

print(list(filter(lambda x:students[x]>=80,students)))



# Map Function in python 

# A map fucntion in python basically helps us to transform every element from a itertor based on the codition and return the transformed iterator.


# It taks two thing function whcih return the result of every elemt based on the logic given and the second is the iterator 

L=[1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x:x**2,L))) 


print(list(map(lambda x:"yes" if x%2==0 else "no",L)))



z1=[1,2,3]

z2=[2,3,3,5]


ans = map(lambda x,y:x+y,z1,z2)
print(list(ans))   # only first 3 elemnts are being used 


print(list(ans))


# reduce function:-- 

L=[1,2,3,4,5,6,7,8,9,10]

print(reduce(lambda a,b:a+b,L))



























































































































