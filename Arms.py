r=int(input())
s=r
t=0
while(r>0):
  v=r%10
  r=r//10
  d=v**3
  t=t+d
if(s==t):
  print('yes')
else:
    print('no')
