lst=[]
num=int(input("How many numbers:"))
 for n in range (num):
  numbers=int(input("enter number:"))
  lst.append(numbers)
  print("minimum element in the list is:",min(lst))
