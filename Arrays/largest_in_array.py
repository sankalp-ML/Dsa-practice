class Solution:
    def largest(self, arr):
        maxi=arr[0]
        for i in arr:
            if i > maxi:
                maxi = i
        return maxi
    
    

x=Solution()
print(x.largest([5, 5, 5, 5]))