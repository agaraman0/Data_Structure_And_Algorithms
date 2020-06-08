
dp = [[0 for i in range(10)] for j in range(10)]

def minCost(r,c):

	for i in range(r):
		for j in range(c):

			if i == 0 and j == 0:
				dp[i][j] = cost[0][0]

			elif i == 0:
				dp[i][j] = dp[0][j-1] + cost[0][j]

			elif j == 0:
				dp[i][j] = dp[i-1][0] + cost[i][0]

			else:
				dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + cost[i][j]

	return dp[r-1][c-1]

cost = [[1,2,3],[6,5,4],[7,8,9]]

print(minCost(3,3))
print(dp)