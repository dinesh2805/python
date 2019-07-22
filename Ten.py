n1=int(input())
l1=list(map(int,input().split()))
s=0
for i in range(0,len(l1)):
    for j in range(0,i):
        if(l1[j]<l1[i]):
            s=s+l1[j]
print(s)
