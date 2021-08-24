def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr.pop()

    item_greater=[]
    item_lower=[]

    for item in arr:
        if item>pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
    
    return quickSort(item_lower)+[pivot]+quickSort(item_greater)

arr=[-1,100,23,45,1,2,12,-12,-23]
print(quickSort(arr))


