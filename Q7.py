nn,qn=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if(a[i]+a[j]==qn):
        count=1
        break
if(count):
   print("yes")
else:
   print("no")    
