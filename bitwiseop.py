def main():
	try:
		m=int(input())
		k=int(input())
		m=m^k
		k=m^k
		m=m^k
		print(m,k)
	except:
		print('invalid')
main()
