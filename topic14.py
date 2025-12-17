# Recursion 


# recursion limit in python is 1000 

# to see and change recursion limit we use sys module:--



import sys
print(sys.getrecursionlimit())


sys.setrecursionlimit(10**5)

print(sys.getrecursionlimit())


# check prime number using recursion:--



def prime(n,num):
    if n==1:
        return True
    if num%n==0:
        return False
    return prime(n-1,num)

print(prime(12,13))