r1=int(input())
s1=0
t1=[]
for u in range(1,r1+1):
	t1.append(u)
for u in range(len(t1)):
	for u in range(u+1,len(t1)):
		s1+=1
print(s1)
