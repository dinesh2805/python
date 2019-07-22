N1=int(input())
Lk1=list(map(int,input().split()))
A=[1]*N1
for D in range(N1):
    if(D==0):
        if(Lk1[D]>Lk1[D+1]):
            A[D]=A[D]+A[D+1]
    elif(D>0):
        if(Lk1[D]>Lk1[D-1]):
            A[D]=A[D]+A[D-1]
print(sum(A))
