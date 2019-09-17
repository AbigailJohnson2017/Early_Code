x=1
while x<=5:
  print(x)
  if x%2==0:
    y=x/2
  else:
    y=3*x+1
  print(y)
  while y!=1:
    if y%2==0:
      y=y/2
    else:
      y=3*y+1
    print(y)
  if y==1:
    print('Yes')
  x=x+1
