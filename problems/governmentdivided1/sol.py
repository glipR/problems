T = int(input())

fac = [0] * 2000001
pr = []

for i in range(2, 2000001):
    if fac[i] == 0:
        fac[i] = i
        pr.append(i)
    for p in pr:
        if p > fac[i] or i * p > 2000000:
            break
        fac[i * p] = p

def fast_factors(n):
    res = []
    while n > 1:
        f = fac[n]
        n //= f
        if len(res) == 0 or res[-1][0] != f:
            res.append([f, 1])
        else:
            res[-1][1] += 1
    return res

for _ in range(T):
    n = int(input())
    facs = fast_factors(n)
    ways = 1
    for f, c in facs:
        ways *= c + 1
    print(ways)
