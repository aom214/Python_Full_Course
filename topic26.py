#Abstarction:- It basically means hiding comlex implementation deatil and showing only necessary one for example in upi payment you only see money is being send or not not the complex queries being executed inside it.

#python does not have built in absatrct class 

# In python we import it using abc module 

from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass 


class upi(payment):
    def pay(self,amou):
        pass


        
u1=upi()

u1.pay(2)