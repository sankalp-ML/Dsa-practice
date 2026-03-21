#manual way
class Solution:
    def findMaximum(self, arr):
		
        maxi=arr[0]
        for i in arr:
            if i>maxi:
                maxi=i
        return maxi
    
    
x=Solution()
arr=[1, 2, 4, 5, 7, 8, 3]
print(x.findMaximum(arr))
        
#direct method
print(max(arr))