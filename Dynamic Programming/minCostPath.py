
dpMin = [[0 for i in range(10)] for j in range(10)]

def minCost(r,c):

	for i in range(r):
		for j in range(c):

			if i == 0 and j == 0:
				dpMin[i][j] = cost[0][0]

			elif i == 0:
				dpMin[i][j] = dpMin[0][j-1] + cost[0][j]

			elif j == 0:
				dpMin[i][j] = dpMin[i-1][0] + cost[i][0]

			else:
				dpMin[i][j] = min(dpMin[i-1][j],dpMin[i][j-1]) + cost[i][j]

	return dpMin[r-1][c-1]

dpMax = [[0 for i in range(10)] for j in range(10)]

def maxCost(r,c):

	for i in range(r):
		for j in range(c):

			if i == 0 and j == 0:
				dpMax[i][j] = cost[0][0]

			elif i == 0:
				dpMax[i][j] = dpMax[0][j-1] + cost[0][j]

			elif j == 0:
				dpMax[i][j] = dpMax[i-1][0] + cost[i][0]

			else:
				dpMax[i][j] = max(dpMax[i-1][j],dpMax[i][j-1]) + cost[i][j]

	return dpMax[r-1][c-1]

cost = [[1,2,3],[6,5,4],[7,8,9]]

print(minCost(3,3))
print(dpMin)

print(maxCost(3,3))
print(dpMax)