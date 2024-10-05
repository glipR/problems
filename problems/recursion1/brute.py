MOD = int(1e9+7)

n = int(input())

f1, f2 = 1, 1
for x in range(n-1):
    f1, f2 = (f1+f2) % MOD, f1

print(f1)
