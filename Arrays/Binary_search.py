class Solution:
    def Binary_Search(self,arr,x):
        
        for i in range(len(arr)-1):
             if arr[i] > arr[i+1]:
                break
        arr.sort()
        
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low+high) // 2
            
            if arr[mid] == x:
                return mid
            elif x > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

      
        



x=Solution()
print(x.Binary_Search([2,1,3,4],1))
            
            