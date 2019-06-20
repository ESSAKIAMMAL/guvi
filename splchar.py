w=input()
i=0
for a in range (len(w)):
 if(w[a].isdigit() or w[a].isalpha() or w[a]==' '):
  continue
 else:
  i+=1
print(i)  
