while True:
	print("Enter 'x' for exit.")
	num = input("Enter a number: ")
	if num == 'x':
		break
	else:
		number = int(num)
		for i in range(2, number-1):
			if number%i == 0:
				print(i)
				i += 1
