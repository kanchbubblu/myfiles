num = int(input("enter any num:"))
if num >1:
  for i in range (2,num):
   if (num%i)==0:
     print(num,"is a composite")
     break
     else:
       print(num,"is a prime")
