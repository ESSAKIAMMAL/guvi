nu=int(input())
l,r=map(int,input().split())
for i in range(l+1,r):
    if(i==nu):
        print("yes")
        break
else:
  print("no")
