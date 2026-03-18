#manual solution
class Solution:
    def getAlternates(self, arr):
        
        m=[]
        for i in range(len(arr)):
            if i%2==0:
                m.append(arr[i])
        return m
    

c=Solution()
arr=[1, 2, 3, 4]
print(c.getAlternates(arr))


#direct method
print(arr[::2])