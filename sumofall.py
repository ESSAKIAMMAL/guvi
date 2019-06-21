bc=int(input())
s=0
while(bc>0):
  r=bc%10
  s=s+r
  bc=bc//10
print(s)
