MOD = int(1e9+7)

g1 = 1
g0 = 0

n = int(input())
for _ in range(n):
    g1, g0 = (3*g1 + g0) % MOD, g1

print(g0)
