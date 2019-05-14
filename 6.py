a,b = input().split()
c = len(set(list(a)))
b = len(set(list(b)))
if b == c:
  print("yes")
else:
  print("no")
