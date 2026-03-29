class Solution:
    def countZeroes(self, arr):
        count=0
        for i in range(len(arr)):
            if arr[i]==0:
                count=len(arr)-i
                break
        return count      
                
x=Solution()
print(x.countZeroes([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]))