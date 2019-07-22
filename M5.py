atj1=int(input())
btj1=pow(2,atj1)
ztj1=[]
for i in range(btj1):  
    mtj1=bin(i).replace("0b","")
    ztj1.append(mtj1.zfill(atj1))
    ztj1.sort(key=(lambda x:x.count('1')))
for i in ztj1:
    print(i)
