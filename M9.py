ay=int(input())
by=[int(s) for s in input().split()]
by.sort()
s=0
xv=0
for i in range(len(by)):
    if by[i]>=s:
        xv+=1
    s=s+by[i]
print(xv)
