a=[]
n=int(input("enter the num of elements:"))
for i in range(1,n+1):
   b=int(input("enter the elements:"))
   a.append(b)
 a.sort()
 print("Largest element is:",a[n-1])
 
