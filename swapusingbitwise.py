def max():
   	k=int(input())
   	b=int (input())
   	c=int(input())
   	if (k>b):
      if(k>c):
    			print (k)
   		else :
    			print(c)
   	elif (b>c):
   		print (b)
   	else:
   		print (c)
def main():
   	try:
    		max()
   	except ValueError:
    		print('invalid')
main()
