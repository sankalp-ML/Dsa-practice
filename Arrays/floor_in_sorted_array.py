class Solution:
    def findFloor(self, arr, x):
        index=-1
        for i in range(len(arr)):
            if arr[i]<=x:
                index= i
            else:
                break
        return index
            
            
x=Solution()
print(x.findFloor([1, 2, 8, 10, 10, 12, 19], x = 5))