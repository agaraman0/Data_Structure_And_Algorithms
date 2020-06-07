class DSU(object):

	def __init__(self,n):
		self.parent = [i for i in range(0,n+2)]
		self.rank  = [0]*(n+1)
		self.total = n

	def getParent(self,a):

		if a == self.parent[a]:
			return a
		x = self.getParent(self.parent[a]);
		self.parent[a] = x
		return x

	def unionSet(self,a,b):

		a = self.getParent(a)
		b = self.getParent(b)

		if a != b:
			if self.rank[a]<self.rank[b]:
				a,b = b,a
			self.parent[b] = a
			if self.rank[a] == self.rank[b]:
				self.rank[a]+=1
				self.total-=1

dsu = DSU(8)
dsu.unionSet(1,2)
dsu.unionSet(3,4)

print(dsu.getParent(1),dsu.getParent(2),dsu.getParent(3),dsu.getParent(4))

dsu.unionSet(2,3)

print(dsu.getParent(1),dsu.getParent(2),dsu.getParent(3),dsu.getParent(7))