eh=input()
ei=False
ee=False
for i in eh:
  if(i.isdigit()):
    ei=True
  if(i.isalpha()):
   ee=True
if(ei and ee):
    print("Yes")
else:
    print("No")
