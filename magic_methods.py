class adding:
    def __init__(self,i,j):
        self.i=i 
        self.j=j
    def __add__(b,a):
        return adding(a.i+b.i,a.j+b.j)
    
z1 = adding(10,20)

z2 = adding (100,200)

print(z1+z2+z2)



class adding:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def __call__(self):
        return self.a+self.b 
    

z = adding(1,2)

print(z())

