# H(n) = sum^(n-1)_{i=1} (N-i)^2F(i) + 4H(n-1)
MOD = int(1e9+7)

n = int(input())
h = 0

for x in range(1, n+1):
    h *= 4
    h %= MOD
    f1, f2 = 1, 0
    for i in range(1, x):
        h += (x-i) * (x-i) * f1
        h %= MOD
        f1, f2 = (f1+f2)%MOD, f1
print(h)
