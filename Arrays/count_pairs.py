class optimizedSol:
    def countAllPairs(self, arr, target):
        freq = {}
        count = 0

        for num in arr:
            need = target - num
            if need in freq:
                count += freq[need]
    
            freq[num] = freq.get(num, 0) + 1

        return count


c = optimizedSol()
print(c.countAllPairs([1, 5, 7, -1, 5], target = 6))