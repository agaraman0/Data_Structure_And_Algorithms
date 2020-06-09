
order = []
visited = [0]*(10**5)
component = []

def dfs(node):

	visited[node] = 1

	for children in graph[node]:
		if visited[children] == 0:
			dfs(children)

	order.append(node)

def dfs_helper(node,comp_no):
	visited[node] = 1
	component