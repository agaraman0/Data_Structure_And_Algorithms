# https://leetcode.com/problems/maximum-product-subarray/

def maxProduct(arr):
    n = len(arr)
    
    if n == 1:
        return arr[0]
    
    maxEnd = 1
    minEnd = 1
    mx = 1
    flag = 0
    flmx = 0
    
    for i in range(n):
        if arr[i] > 0:
            maxEnd = maxEnd*arr[i]
            minEnd = min(minEnd*arr[i],1)
            flmx = 1
            
        elif arr[i] == 0:
            minEnd = 1
            maxEnd = 1
            flag = 1
        elif arr[i]<0:
            temp = maxEnd
            maxEnd = max(minEnd*arr[i],1)
            minEnd = temp*arr[i]

        if maxEnd>mx:
            mx = maxEnd
            
            
        # print(maxEnd,minEnd,mx)
    
    if flag and flmx==0 and mx==1:
        return 0
    
    return mx