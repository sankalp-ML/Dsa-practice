def decrementList(arr):
    m=[]
    for i in arr:
        i -= 1
        m.append(i)
    return m


arr=[54, 43, 2, 1, 5]
print(decrementList(arr))