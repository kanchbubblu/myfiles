string=input("Enter string:")
mycount=0
for i in string:
      if(i.isdigit()):
          mycount=mycount+1
print("The number of digits is:")
print(mycount)
