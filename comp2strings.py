def compare(str1,str2):
	if str1==str2:
		print(str2)
	elif str1>str2:
		print(str1)
	else :
		print(str2)
def main():
	try:
		k1=input()
		k2=input()
		compare(k1,k2)
	except:
		print('invalid')
main()
