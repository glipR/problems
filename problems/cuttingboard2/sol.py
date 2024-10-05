MAX_N = int(2e6)

is_prime = [True] * (MAX_N+1)
is_prime[0] = False
is_prime[1] = False

for jump in range(2, MAX_N+1):
    if not is_prime[jump]: continue
    for pos in range(2*jump, MAX_N+1, jump):
        is_prime[pos] = False

primes = [i for i, v in enumerate(is_prime) if v]

def n_prime_factors(v):
    n_factors = 0
    for p in primes:
        while v % p == 0:
            v //= p
            n_factors += 1
    return n_factors

n, m = list(map(int, input().split()))

n_factors = n_prime_factors(n)
m_factors = n_prime_factors(m)

if n_factors > m_factors:
    print("Vaughn")
elif m_factors > n_factors:
    print("Hazel")
else:
    print("2nd Player")

