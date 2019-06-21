str=input()
n=False
m=False
for i in str:
    if(i.isdigit()==True):
        m=True
    if(i.isalpha()==True):
        n=True
if(n and m):
    print("Yes")
else:
    print("No")
