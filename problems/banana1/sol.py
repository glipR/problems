import math

N, c = list(map(int, input().split()))

am = 0
for _ in range(N):
    am += int(input())

print(c * math.ceil(am/10))

