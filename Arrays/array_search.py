class Solution:
    def search(self, arr, x):
        
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
    
    
A=Solution()
print(A.search([1, 3, 3, 4], x = 3))