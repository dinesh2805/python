abc,ab1c=list(map(int,input().split()))
cb1=list(map(int,input().split()))
cb=[]
while(ab1c):
    m = list(map(int,input().split()))
    cb.append(m)
    ab1c-=1
for j in cb:
    val=0
    for k in range(j[0]-1,j[1]):
        val=val^cb1[k]
    print(val)
