arr = [int(temp) for temp in input().strip().split(' ')]

def insertion(arr):
    for i in range(1,len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                pass
    return arr

print(insertion(arr))
