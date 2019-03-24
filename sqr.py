def square():
	min=999
	(a,b) = ([],[])
	for i in range(4):
		for j in range(2):
			b.append(int(input()))
		a.append(l)
		for m in b:
			if min > m:
				min = m
		b = []
	f = 1
	for i in range(len(a)):
		dif = a[i][0]-a[i][1]
		if dif in(0,-min,min):
			continue
		else :
			f = 0
			break
	if f != 0:
		print('yes')
	else :
		print('no')
try:
	square()
except:
	print('invalid')
