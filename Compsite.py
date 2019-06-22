pea=int(input())
if pea>0:
  for x in range(2,pea):
    if(pea%x==0):
      print("yes")
      break
  else:
    print("no")
else:
  print("yes")
