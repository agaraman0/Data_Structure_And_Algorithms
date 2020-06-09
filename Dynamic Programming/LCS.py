m = len(text1)
n = len(text2)
dp = [[0 for i in range(n+1)] for i in range(m+1)]

def LCS(text1,text2,m,n):
    
    # print(m,n)
    if m == 0 or n == 0:
        return 0;
    
    if dp[m][n]>0:
        return dp[m][n]
    
    if text1[m-1] == text2[n-1]:
        dp[m][n] = 1 + LCS(text1,text2,m-1,n-1)
    
    else:
        dp[m][n] = max(LCS(text1,text2,m-1,n),LCS(text1,text2,m,n-1))

    return dp[m][n]
