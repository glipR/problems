import sys

n = int(input())

lights = [False] * (n+1)
for x in range(1, n+1):
    for pos in range(x, n+1, x):
        lights[pos] = not lights[pos]

print(lights, file=sys.stderr)
print(sum(lights))
