import copy 

L = [[1,2],[3,4]]

shall_copy = copy.copy(L)
deep_copy = copy.deepcopy(L)
print(id(L),id(L[0]))
print(id(shall_copy),id(shall_copy[0]))
print(id(deep_copy),id(deep_copy[0]))  #deep copy 


z=L.copy()

print(id(z),id(z[0]))   # so shallow copy
