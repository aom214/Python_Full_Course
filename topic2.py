#               Enumerator

# Enumerator basically helps us to track index while iterating over List, tuple or string something for example if we want to track index while iterating over the list then we use enumartor 

L=['Cricket','Football','BasketBall','HandBall']
# for example 

# whithout enumartor you write 

for i in range(len(L)):
    print(i,L[i])

# using enumartor you write 
for pos,elm in enumerate(L,1):
    print(pos,elm)


#It also helps us to convert list directly to dictionary using it and also to conver it to the json 

#for example 

dic = dict(list(enumerate(L,1)))

print(dic)



# 🚀 Why use enumerate()?

# Because it helps you:

# Avoid manually managing counters (i = 0, i += 1).

# Write cleaner and shorter loops.

# Prevent off-by-one errors in indexing.


s="abcd"
t=('a','b','c','d')
print(list(enumerate(s,1)))
print(list(enumerate(t,1)))