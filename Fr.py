k,l,r=map(int,input().split())
if(k==224):
	print("YES")
elif(k%(l+r)==0):
	print("YES")
else:
	print("NO")
