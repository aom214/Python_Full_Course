# # exception handling questions


# #question 1:- Q. write a python program that will sum numbers present in
# # given list of data.
# # expected output:-
# # enter the list:- [1 ,'a','b',3]
# # item 'a' is not a number.
# # item 'b' is not a number
# # 4



# L= list(str(input()).split())
# s=0
# for i in range(len(L)):
#     try:
#         s+=int(L[i])
#     except Exception as e:
#         print(e)
        
# print(s)


num=[1,2,3,4,5,6]

def n():
    try:
        number = int(input())
        print(num[number])
    except Exception as e:
        print(e)
        n()
n()