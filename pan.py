def checkpanag(str):
	a = []
	for i in range(26):
		a.append(False)
	for s in str.lower():
		if s != ' ':
			a[ord(s)-ord('a')]=True
	for c in a:
		if c == False:
			return False
	return True
  
def main():
	s=input()
	print(checkpanag(s))
try:
	main()
except:
	print('invalid')
