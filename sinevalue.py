import math
def sin(x):
    sine = 0
    for i in range(x):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine
x=int(input("Enter the value of x in degrees:"))
print(round(sin(x),2))
