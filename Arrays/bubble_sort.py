class Solution:
    def bubble_sort(self,arr):
        n=len(arr)
        for i in range(n):
            swapped=False
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped=True
            if swapped==False:
                break
        return arr  
            
x=Solution()
print(x.bubble_sort([2,1,4,3,4,5,6,7]))
                