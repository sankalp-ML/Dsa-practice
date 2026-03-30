class Solution():
    def firstfreq(self,arr):
        freq={}
        for i in arr:
            freq[i] = freq.get(i, 0)+1
        print(freq)
        
        for i in arr:
            if freq[i] == 1:
                return i
            
            
            
x=Solution()
print(x.firstfreq([1,2,1,2,3]))
                

        
    