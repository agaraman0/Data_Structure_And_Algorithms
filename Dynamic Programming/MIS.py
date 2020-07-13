

def maximIncSub(arr):

	n = len(arr)

	mx = 0

	dp = [i for i in arr]

	for i in range(1,n):

		for j in range(0,i):

			if arr[i]>arr[j] and dp[j]+arr[i]>dp[j]:

				dp[i] = max(dp[j]+arr[i], dp[i])

		mx = max(dp[i],mx)


	return mx

arr = [1, 101, 2, 3, 100, 4, 5]

print(maximIncSub(arr))