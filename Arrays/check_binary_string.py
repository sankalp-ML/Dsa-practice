class Solution:
    def isBinary(self, s):
        for ch in s:
            if ch != '0' and ch != '1':
                return False
        return True      
            
x=Solution()
print(x.isBinary('101'))

class Solution:
    def binary(self, s):
        return set(s).issubset({'0', '1'})
    
x=Solution()
print(x.binary('101'))