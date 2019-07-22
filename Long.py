M=int(input())
K1=[]
for X1 in range(0,M):
   K1.append(input())
L3=len(K1[0])
S1=""
for X1 in range(0,L3):
   C1=K1[0][X1]
   F1=0
   for Y1 in range(0,M):
        if(C1!=K1[Y1][X1]):
           F1=1
   if(F1==0):
     S1=S1+C1
   else:
     break
print(S1)
