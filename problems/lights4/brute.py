import sys

n = int(input())

lights = [0] * (n+1)
for x in range(1, n+1):
    for pos in range(x, n+1, x):
        lights[pos] += 1

is_prime = [True] * (n+1)
is_prime[0] = False
is_prime[1] = False
for x in range(2, n+1):
    if not is_prime[x]: continue
    for pos in range(2*x, n+1, x):
        is_prime[pos] = False

# print(lights, file=sys.stderr)
prime_lights = [is_prime[l] for l in lights]
# print(prime_lights, file=sys.stderr)
print(sum(prime_lights))
