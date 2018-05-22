a=list(input())
b=list(input())
m=len(a)
d=0
i=0
while m>0:
    d=d+(ord(b[i])-ord(a[i]))
    i=i+1
    m=m-1
print(d)
