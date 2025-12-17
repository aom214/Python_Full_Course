# class Solution:
#     def findTwoElement(self, arr):
#         missing=-1
#         double=-1
#         for i in range(len(arr)):
#             curr = arr[i]
#             while curr!=i+1:
#                 if curr == arr[curr-1]:
#                     double = curr
#                     missing = i+1
#                     break
#                 else:
#                     arr[i]=arr[curr-1]
#                     arr[curr-1] = curr
#                 curr = arr[i]
#         return [double,missing]
# c1=Solution()
# print(c1.findTwoElement([11,1,8,5,2,4,5,7,16,9,13,14,3,17,15,6,12]))



class Solution:
    def constructArr(self, arr):
        l=-1
        for i in range(1,len(arr)+1):
            if (i*(i+1))//2==len(arr):
                l=i
                break
        if l==-1:
            return False
        z=[0]*(l+1)
        if len(arr)==1 and arr[0]>0:
            return True
        z[0] = (arr[0]+arr[1]-arr[2])//2
        for i in range(1,l+1):
            z[i]=arr[i-1]-z[0]
        return z
    

s=Solution()

print(s.constructArr([6,4,4,8,8,6]))




