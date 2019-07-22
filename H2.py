at1=(input())
catat=0
for i in range(0,len(at1)):
    surat=(at1[:i]+at1[i+1:])
    if(int(surat) % 8==0):
        catat=1
        break
if(catat==1):
    print("yes")
else:
    print("no")
