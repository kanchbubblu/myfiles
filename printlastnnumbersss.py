t=input("Enter a string and N value:")
st=t.split(" ")[0][::-1]
n=int(t.split(" ")[1])
ans=''
for x in range(n):
	ans=ans+st[x]
print(ans)
