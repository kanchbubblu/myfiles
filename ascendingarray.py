n=int(input("Enter N value:"))
print("Enter the ascending with one change array:")
a=[]
for x in range(n):
	m=int(input())
	a.append(m)
for x in range(n-1):
	for y in range(x,n):
		if(a[x]>a[y]):
			ans=x+1
print(ans)
