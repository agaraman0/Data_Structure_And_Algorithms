# https://leetcode.com/problems/edit-distance/submissions/
dp = [[-1 for x in range(len(word2)+1)] for y in range(len(word1)+1)]
        
        for x in range(len(word2)+1):
            dp[0][x] = 0
        for y in range(len(word1)+1):
            dp[y][0] = 0
        
        def editDistance(word1,word2,m,n):
            
            if m == 0:
                return n
            if n == 0:
                return m
            
            if dp[m][n] > -1:
                return dp[m][n]
            
            if word1[m-1] == word2[n-1]:
                dp[m][n] = editDistance(word1,word2,m-1,n-1)
            
            else:
                dp[m][n] = 1+min(editDistance(word1,word2,m-1,n-1),editDistance(word1,word2,m-1,n),editDistance(word1,word2,m,n-1))
            return dp[m][n]
        
        return editDistance(word1,word2,len(word1),len(word2))