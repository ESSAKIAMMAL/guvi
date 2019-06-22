
  
re = input()
b = ["a","e","i","o","u","A","E","I","O","U"]
c=len(re)
for i in range(0,c):
  if(re[i] in b):
    print("yes")
    break
else:
  print("no")
