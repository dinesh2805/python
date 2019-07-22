def sub1(rt23): 
    mt = len(rt23) 
    sub1 = [1]*mt 
    for i in range (1 , mt): 
        for j in range(0 , i): 
            if rt23[i] > rt23[j] and sub1[i]< sub1[j] + 1 : 
                sub1[i] = sub1[j]+1
    maximum = 0
    for i in range(mt): 
        maximum = max(maximum , sub1[i])  
    return maximum
ar1=int(input()) 
rt23 = list(map(int,input().split()))
print (sub1(rt23))
