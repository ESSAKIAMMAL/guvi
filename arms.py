r,e=map(int,input().split())
for i in range(r,e):
    l=len(str(i))
    s=0
    temp=i
    while(i>0):
        x=i%10
        s=s+(x**l)
        i=i//10
    if(s==temp):
        print(s,end=" ")
