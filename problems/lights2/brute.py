import math
import sys

n = int(input())
l2 = math.floor(math.log2(n))

lights = [False] * (n+1)
for x in range(0, l2+1):
    jump = (1 << x)
    for pos in range(jump, n+1, jump):
        lights[pos] = not lights[pos]

print(lights, file=sys.stderr)
print(sum(lights))
