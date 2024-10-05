import random

# Python solution copied below.

EXCEEDED = False

MAX_FACT = 10000
MAX_K = 30
MOD = 1000000007

fact = [-1] * (MAX_FACT + 1)

fact[0] = 1
fact[1] = 1
for i in range(2, MAX_FACT + 1):
    fact[i] = (fact[i - 1] * i) % MOD

def expmod(a, b):
  res=1
  a %= MOD
  while b:
    if (b&1):
      res=(res*a)%MOD
    b //= 2
    a=(a*a)%MOD
  return res

def inv(a):
    return expmod(a, MOD - 2)

def nCk(a, b):
    if b > MAX_FACT:
        raise ValueError("Does not fit problem description.")
    # b (num distinct - 1) is always quite small <= 10000.
    if a > MAX_FACT:
        res = 1
        for i in range(b):
            res *= a - i
            res %= MOD
        res = res * fact[b] % MOD
        return res
    return fact[a] * inv(fact[b]) * inv(fact[a-b]) % MOD

def slow_factors(a):
    res = []
    i = 2
    while i * i <= a:
        if (a % i == 0):
            res.append([i, 0])
            while (a % i == 0):
                a //= i
                res[-1][1] += 1
        i += 1
    if (a > 1):
        res.append([a, 1])
    return res

from collections import defaultdict
DP = [defaultdict(lambda: -1) for _ in range(MAX_K+1)]

def solve(fac_counts, n, k):
    if len(fac_counts) == 0 and n == 1:
        return 1
    if DP[k][n] != -1:
        return DP[k][n]
    if k == 0:
        DP[k][n] = 1
        return DP[k][n]
    total = 0
    # Try any possible selection of fac_count elements.
    counters = [0] * len(fac_counts)
    new_counts = [0] * len(fac_counts)
    while counters[0] <= fac_counts[0][1]:
        cur = n
        for x in range(len(counters)):
            if counters[x] > 0:
                cur //= fac_counts[x][0] * counters[x]
            new_counts[x] = [fac_counts[x][0], fac_counts[x][1] - counters[x]]
        distinct = solve(new_counts, cur, k-1)
        # Number of distinct = n // cur stars, distinct - 1 bars.
        if distinct == 1:
            total = (total + 1)
        else:
            total = (total + nCk(n // cur + distinct - 1, distinct - 1))
        counters[-1] += 1
        c = len(counters) - 1
        while c >= 1 and counters[c] > fac_counts[c][1]:
            counters[c] = 0
            c -= 1
            counters[c] += 1
    DP[k][n] = total
    return DP[k][n]

N_EASY = 3
N_MEDIUM = 7
N_HARD = 20
for x in range(1, N_EASY+1):
    n = random.randint(1, 20)
    fac_counts = slow_factors(n)
    for k in range(1, 11):
        r = solve(fac_counts, n, k)
        DP = [defaultdict(lambda: -1) for _ in range(MAX_K+1)]
        if r <= 10000:
            continue
        break 
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{n} {k}\n")
for x in range(N_EASY+1, N_EASY + N_MEDIUM+1):
    n = random.randint(20, 5000)
    fac_counts = slow_factors(n)
    for k in range(1, 11):
        r = solve(fac_counts, n, k)
        DP = [defaultdict(lambda: -1) for _ in range(MAX_K+1)]
        if r <= 10000:
            continue
        break 
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{n} {k}\n")
for x in range(N_EASY + N_MEDIUM+1, N_EASY + N_MEDIUM + N_HARD + 1):
    n = random.randint(5000, 1000000000000)
    fac_counts = slow_factors(n)
    for k in range(1, 11):
        r = solve(fac_counts, n, k)
        DP = [defaultdict(lambda: -1) for _ in range(MAX_K+1)]
        if r <= 10000:
            continue
        break 
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{n} {k}\n")

