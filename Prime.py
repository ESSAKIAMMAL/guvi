m,n=list(map(int,input().split()))
for g in range(m+1,n):
  for h in range(2,g):
    if g%h==0:
      break
  else:
    print(g,end=" ")
