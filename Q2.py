S1k,T1k = map(int,input().split())
L11k = []
L21k = []
L11k = input().split()
for D in range(len(L11k)):
    L11k[D] = int(L11k[D])
for D in range(T1k):
    A,B = map(int,input().split())
    res = 0
    for D in range(A-1,B):
        res += L11k[D]
    print(res)
