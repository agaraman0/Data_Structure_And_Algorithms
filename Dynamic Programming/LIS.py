# https://leetcode.com/problems/longest-increasing-subsequence/
def lengthOfLIS(arr):
        
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return 1     
        dp = [1]*n
        
        mx = 1
        
        for i in range(1,n):
            for j in range(0,i):
                if arr[i]>arr[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            
            mx = max(dp[i],mx)
        
        return mx