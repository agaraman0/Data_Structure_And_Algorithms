arr = [int(temp) for temp in input().strip().split(' ')]

def bubblesort(arr):
    while True:
        a = 0
        for i in range(len(arr)-1):
            temp = i;temp_a = i+1
            if arr[temp] > arr[temp_a]:
                arr[temp],arr[temp_a]=arr[temp_a],arr[temp]
                a = a+1
        if a == 0:
            return arr

print(bubblesort(arr))

            
