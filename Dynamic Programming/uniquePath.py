def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        dp = [[0]*(101) for i in range(101)]
        m = len(grid)
        n = len(grid[0])
        
        if m<2 and n<2:
            if grid[0][0] == 1: 
                return 0
            else:
                return 1
        if grid[m-1][n-1]:
            return 0
        
        def unique(m,n):
            
            if m==0 and n == 0:
                return 1
            if m<0 or n<0:
                return 0
            if dp[m][n]>0:
                return dp[m][n]
            
            if grid[m-1][n]:
                ans1 = 0
            else:
                ans1 = unique(m-1,n)
                
            if grid[m][n-1]:
                ans2 = 0
            else:
                ans2 = unique(m,n-1)
            
            dp[m][n] = ans1+ans2
            
            return dp[m][n]
        
        return unique(len(grid)-1,len(grid[0])-1)