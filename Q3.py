nn, kn = input().split()
nn, kn = int(nn), int(kn)
o = [int(x) for x in input().split()]
for i in range(0, kn):
    a, b = input().split()
    a, b = int(a), int(b)
    print(min(o[a-1:b]))
