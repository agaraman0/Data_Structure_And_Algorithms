
def recurKnapsack(profit, weight, capacity, i):

	if i == len(profit):
		return 0

	if capacity<0:
		return 0

	mx = 0

	if capacity>=weight[i]:

		mx = max(recurKnapsack(profit,weight,capacity-weight[i],i+1)+profit[i],recurKnapsack(profit,weight,capacity,i+1))

	print(capacity)
	print(mx)

	return mx

profit = [1,6,10,16]
weight = [1,2,3,5]

capacity = 7


dp = [[0 for i in range(capacity+1)] for j in range(len(profit))]

def dpKnapsack(profit, weight, capacity, i):

	if i == len(profit):
		return 0

	if capacity<0:
		return 0

	if dp[i][capacity] > 0:
		return dp[i][capacity]

	if capacity>=weight[i]:

		dp[i][capacity] = max(dpKnapsack(profit,weight,capacity-weight[i],i+1)+profit[i],dpKnapsack(profit,weight,capacity,i+1))

	# print(capacity)
	# print(mx)

	return dp[i][capacity]



print(dpKnapsack(profit,weight,capacity,0))