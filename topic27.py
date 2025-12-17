# Exception handling in python:--


# In python to handle exception we basically have 4 thing try, except, else and finally


# inside try we write our code which we have to execte and see if there is some exception or not 

# except will caught exception that occurs in code inside try block

# if no exception occur then else will run 


# fianally will always run either exception occur or not and we basically use it to clos connection with db andto close the files which are previously opened in try block



try:
    pass
except:
    pass 
else:
    print("It gets executed which says there is no error in the code which we have written")
finally:
    print("code executed completelly")



try:
    print("hello world")
except Exception as e:
    print(f"error description is :- {e}")
    print(f"error class is :- {e.__class__}")




# raise keyword in python :-- exception can be raise forcelly by using raise keyword 


# user defined exceptions :- These are the exceptions created by programmers for example if your account have 10000 rupees and you are trying to withdraw 20000 then this will raise an exception which is defined by programmers




try:
    age = int(input())
    if age<=0:
        raise ValueError("invalid age")
    print(f"age is :- {age}")
except Exception as e:
    print("Exception Description is :- ",e)



# creating own exceptions:--


class Dividebyfive(Exception):
    pass

try:
    n1=int(input("Enter number 1:- "))
    n2=int(input("Enter number 2:- "))
    if n2==5:
        raise Dividebyfive("Cannot Divide By 5 Exception")
    print(n1/n2)
except Exception as e:
    print(e)




#exception ahndlieng example using bank example min balance should be 1000 rs and user will be blocked if attempt wrong pin for 4 times  

p="1234"
curr_amount=10000

class maxLimit(Exception):
    pass
class wrongPinError(Exception):
    pass

count=0

def widhdraw(amount):
    curr_amount=10000
    try:
        pin()
        if curr_amount-amount<1000:
            raise maxLimit(" Not enought balance in your account")
        curr_amount-=amount
        print("Money widhdrawal successfully current balance is :- ",curr_amount)
    except Exception as e:
        print("Exception :- ",e)
def pin():
    global count
    n=str(input("enter your pin:-"))
    if n!=p:
        count+=1
        if count>=3:
            raise maxLimit("Maximum limit to eneter pin reached")
        z = input("You enetr wrong pin type y if you want to enter it again:-").lower()
        if z=="y":
            widhdraw(12000)
            raise wrongPinError("Your entered pin is wrong")
        else:
            raise wrongPinError("Your entered pin is wrong")
    else:
        return True
        
        


widhdraw(12000)