h=int(input())
z=0
for i in range(0,h):
  if(pow(2,i)>h):
    break
  z=h-pow(2,i)
print(z)
