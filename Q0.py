import sys 
def Coinsi(ci, mo, V): 
    if (V == 0): 
        return 0
    res = sys.maxsize 
    for i in range(0, mo): 
        if (ci[i] <= V): 
            sub_res = Coinsi(ci, mo, V-ci[i]) 
            if (sub_res != sys.maxsize and sub_res + 1 < res): 
                res = sub_res + 1 
    return res
n,V=list(map(int,input().split()))
ci = list(map(int,input().split())) 
mo= len(ci) 
print(Coinsi(ci, mo, V)) 
