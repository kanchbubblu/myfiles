def countd(k):
	print(k+1)
def main():
	try:
		k=int(input())
		countd(k)
	except:
		print('invalid')
main()
