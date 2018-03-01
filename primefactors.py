n=int(input("Enter an integer:"))
print("Factors are:")
i=1
while(i<=n):
    b=0
    if(n%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                b=b+1
            j=j+1
        if(b==2):
            print(i)
    i=i+1
