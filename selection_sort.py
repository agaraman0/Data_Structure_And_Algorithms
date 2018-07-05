arr = [int(s_temp) for s_temp in input().strip().split(' ')]

def selectionsort(arr):
    temp =[]
    for i in range(len(arr)):
        temp.append(min(arr))
        arr.remove(min(arr))
    return temp

print(selectionsort(arr))
