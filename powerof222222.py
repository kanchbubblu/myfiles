try:
	m=int(input())
	for i in range(m):
		p=2**i
		if p>m:
			print(p)
			break
except:
	print('invalid')
