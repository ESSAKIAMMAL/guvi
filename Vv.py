sut=list(input())
if len(sut)%2==0:
    sut[int(len(sut)/2)] ='*'
    sut[int(len(sut)/2)-1]='*'
else:
    sut[int(len(sut)/2)] ='*'
for i in range(0,len(sut)):
    print(sut[i],end='')
