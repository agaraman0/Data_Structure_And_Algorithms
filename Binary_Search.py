def binarysearch(arr,l,r,x):


    if r>=l:


        mid = int(l+(r-l)/2)

        if arr[mid] == x:
            return mid


        elif arr[mid]> x:

            return binarysearch(arr,l,mid-1,x)


        elif arr[mid]< x:

            return binarysearch(arr,mid+1,r,x)



    else:


        return -1



arr = list(range(101,100001))
result = binarysearch(arr,0,99900,225)
print(result)
