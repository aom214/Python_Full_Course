# List Compherension In Python:--

L=[s*s for s in range(10)]
print(L)


#It is basically a compact way to create the list in poython mostly replacing a for loop


Z=[num*num for num in range(10) if num%2==0]


print(Z)


P=[num*num for num in range(10) if num%2==0 and num%3==0]

print(P)


T=[num*num if num%2==0 else num*num*num for num in range(10)]

print(T)


new = [i*j for i in range(10) for j in range(10)]

print(new)



n=[num*num if num%2==0 else num*6 if num%6==0 else num for num in range(10)]


print("example of if elif else by using chaining", n)


t=["negative" if num<0 else "zero" if num==0 else "positive" for num in range(-2,10)]

print(t)


#dictionary compherension:--

print("-"*50)

print(dict([(num,num*num) for num in range(10)]))


#or 

print({num:num*num for num in range(10)})


print({num:num*num for num in range(10) if num%2==0})


s="aom"

print({i.upper():(ord(i),i) for i in s})

