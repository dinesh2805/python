def mss(arrs):
    inss = 0
    ens = 0

    for i in arrs:
        newen = ens if ens > inss else inss

        inss = ens + i
        ens = newen

    return ens if ens > inss else inss


n = int(input())
o = [int(x) for x in input().split()]
print(mss(o))
