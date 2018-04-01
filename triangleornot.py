def chackValidity(a,b,c):
  if (a+b <=c) or (a+c<=b) or (b+c<=a):
     return False
  else:
     return True
    a=int(input("enter a value:"))
    b=int(input("enter b value:"))
    c=int(input("enter c value:"))
    if checkValidity(a,b,c):
         print("valid")
    else:
         print("invalid")
