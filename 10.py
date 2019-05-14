n,m = raw_input().split()
flag = 0
l = len(n)
if (l==len(m)):
  for i in range(l):
    if(n[i]!=m[i]):
      flag+=1
if (flag==1):
  print("yes")
else:
  print("no")
