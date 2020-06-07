# Number Of BST by N nodes
# Number Of paranthesis

def catlan_recur(n):

	if n<=1:
		return 1;

	ans = 0

	for i in range(1,n+1):

		ans = ans + catlan_recur(i-1) + catlan_recur(n-i)

	return ans


def factorial(n):
	
	if n == 1:
		return 1

	n * factorial(n-1)


# Catlan Formula => (2n)!
# 				-------------
#                 (n+1)! n!   


def catlanByFormula(n):

	return factorial(2n)/(factorial(n+1)*factorial(n))
