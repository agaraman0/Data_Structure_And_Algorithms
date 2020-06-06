def subArraySum(arr, n, tot): 
    #Your code here
    low = 1
    high = 2
    
    total = arr[0]+arr[1]
    
    while(low<high and (low < n or high<=n)):

        if total == tot:
            return low,high
            
        elif total>tot:
            total = total - arr[low-1]
            low = low + 1
        elif total<tot:
            if high != n:
                high = high + 1
                total = total + arr[high-1]
            else:
                return -1
                
    else:
        return -1
