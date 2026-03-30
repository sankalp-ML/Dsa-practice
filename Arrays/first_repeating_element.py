class Solution:
    def firstRepeated(self,arr):
        freq={}
        for i in arr:
            freq[i] = freq.get(i,0)+1
        
        for i in range(len(arr)):
            if freq[arr[i]]>1:
                return i  + 1
        return -1
            
            
x=Solution()
print(x.firstRepeated([1, 5, 3, 4, 3, 5, 6]))