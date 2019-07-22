Hh,pop=input().split()
cost_diff=abs(len(Hh)-len(pop))
for i in range(len(Hh)):
    if len(pop)==1 and pop[i] in Hh:
        break
    if Hh[i] != pop[i]:
        cost_diff+=1 
print(cost_diff)
