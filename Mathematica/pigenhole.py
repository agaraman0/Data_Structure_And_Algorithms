t = int(input())
for i in range(t):

	n = int(input())
	a = [int(i) for i in input().split()]

	d = {i:0 for i in range(n)}

	d[0]+=1
	
	a[0] = a[0]%n

	d[a[0]] +=1


	for i in range(1,n):
		a[i] = (a[i]%n + a[i-1]%n)%n
		a[i] = (a[i]+n)%n

		d[a[i]] += 1

	ans = 0

	# print(d)

	for i in range(n):

		ans = ans + (d[i]*(d[i]-1))//2

	print(ans)
