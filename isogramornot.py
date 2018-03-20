def isogram(n)
 if not isistance (n,str)
    return n,False
  elif len(n)<1:
     return n,False
  n=n.lower()
  if len(n)==len(set(n)):
     return n,True
  else:
     return n,False
