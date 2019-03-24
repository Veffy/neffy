    
def encode(str0,str1):
	(n1,n2) = (len(str0),len(str1))
	(enstr0,enstr1) = ('','')
	for i in range(n1):
		c = ord(str0[i])
		c = c+10
		if c > 122:
			c = c-26
		enstr0 += chr(c)
	enstr1 += str1[0]
	for i in range(1,n2-1):
		c = ord(str1[i])
		c = c+10
		if c > 122:
			c = c-26
		enstr1 += chr(c)
	enstr1 += str1[n2-1]
	print(enstr0,enstr1)
def main():
	try:
		str0 = input()
		str1 = input()
		encode(str0,str1)
	except:
		print('invalid input')
main()
