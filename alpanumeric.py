l1u=input()
E=[]
for i in l1u:
  if(i.isnumeric()):
    E.append(i)
print(*E,sep='')
