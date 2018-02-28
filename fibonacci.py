a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
k=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
while (k-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    k=k-1
