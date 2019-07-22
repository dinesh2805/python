from itertools import combinations
star,uti=map(int,input().split())
l1=len(str(star))
l2=list(combinations(str(star),l1-uti))
l2=sorted(l2)
print(*l2[0],sep='')
