 def pro_51():
	n = int(input())
	a = list(map(int,input().split()))
	for i in range(n):
		prev = a[i]
		co = a
		for j in range(i+a,n):
			if prev >0 and a[j]<0:
				co += a
			elif prev<0 and a[j]>0:
				co += a
			prev = a[j]
		print(co,end=" ")
pro_51()
