import math
a,b=map(int,input().split())
n=[]
v1=list(map(int,input().split()))
for i in range(0,b):
        a1,b1=map(int,input().split())
        n.append([a1,b1])
for i in n:
        x1=i[0]-1
        y1=i[1]-1
        print(math.gcd(v1[x1],v1[y1]))
