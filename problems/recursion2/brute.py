MOD = int(1e9+7)

n = int(input())

f1, f2 = 1, 0
g1, g2 = 5, 0
for x in range(n-1):
    f1, f2 = (f1+f2) % MOD, f1
    g1, g2 = (2*g1 + 3*g2 + f1) % MOD, g1

if n == 0:
    print(g2)
else:
    print(int(g1))
