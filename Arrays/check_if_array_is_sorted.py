class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True
    
    
x=Solution()
print(x.isSorted([10, 20, 30, 40, 50]))