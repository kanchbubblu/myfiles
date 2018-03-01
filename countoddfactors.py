ef countOddSquares(n, m):
    return int(m**0.5) - int((n-1)**0.5)
n=int(input("enter the staring number:"))
m=int(input("enter the ending num:"))
print("Count is", countOddSquares(n, m))
 
