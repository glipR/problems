import math

N, M = list(map(int, input().split()))

am = 0
for _ in range(N):
    am += int(input())

best = 10**40

options = [ list(map(int, input().split())) for _ in range(M)]

to_remove = []
for i, (a, c) in enumerate(options):
    if a >= am:
        best = min(best, c)
        to_remove.append(i)
for i in to_remove[::-1]:
    del options[i]

# Unbounded Knapsack
MAX_IDX = 2 * am
DP = [-1]*(MAX_IDX+1)
DP[0] = 0
for x in range(1, MAX_IDX+1):
    b = 10**40
    for a, c in options:
        if a <= x:
            if DP[x-a] != 10**40:
                b = min(b, DP[x-a] + c)
    DP[x] = b

m = min(best, *DP[am:])
print(m)

