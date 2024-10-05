import sys

sys.setrecursionlimit(int(1e5))

MOD = int(1e9+7)

n = int(input())

DP = [None] * int(1e3 + 5)

# How many parens patterns are there?
def parens(n):
    global calls
    if DP[n] is not None:
        return DP[n]
    if n <= 1:
        return 1
    total = 0
    for x in range(n):
        # There are x parens in the first pattern
        total += (parens(x) * parens(n-x-1)) % MOD
        total %= MOD
    DP[n] = total
    return total

print(parens(n))
