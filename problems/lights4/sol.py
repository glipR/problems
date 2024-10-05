import sys
import math

sys.setrecursionlimit(int(1e5))

n = int(input())

# pi(n) + pi(sqrt(n)) + pi(n^1/4) + ...

prime_limit = int(3e6)

is_prime = [True] * (prime_limit+1)
pi = [0] * (prime_limit+1)
primes = []
is_prime[0] = False
is_prime[1] = False
for x in range(2, prime_limit+1):
    pi[x] = pi[x-1]
    if not is_prime[x]: continue
    pi[x] += 1
    primes.append(x)
    for pos in range(2*x, prime_limit+1, x):
        is_prime[pos] = False

def phi(m, n):
    if m <= prime_limit and pi[m] <= n:
        return 1
    if n == 0:
        return math.floor(m)
    # Try binary searching through a bunch of the easy to solve stuff.
    if n > 50 and m > prime_limit and m//primes[n-1] <= prime_limit and 2*pi[m//primes[n-1]] <= n-1:
        hi = n
        lo = 10
        while hi - lo > 2:
            mid = (hi + lo) // 2
            new_m = m//primes[mid]
            if new_m <= prime_limit and 2*pi[new_m] <= mid:
                # We can go lower
                hi = mid + 1
            else:
                # We can't go this low
                lo = mid + 1
        # Skip from n to mid in n-mid steps, since all deductions will just be -1.
        return phi(m, mid) - (n-mid)
    return phi(m, n-1) - phi(m//primes[n-1], n-1)

def fast_prime(n):
    m = n
    y = math.floor(math.sqrt(m))
    n = pi[y]
    return phi(m, n) + n - 1

total = 0
for x in range(1, math.floor(math.log2(n)) + 1):
    if is_prime[x+1]:
        total += math.floor(fast_prime(math.floor(math.pow(n, 1/x))))
        print(x, total, file=sys.stderr)
print(total)
