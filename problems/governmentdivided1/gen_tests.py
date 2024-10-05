import random

fac = [0] * 10000001
pr = []

for i in range(2, 10000001):
    if fac[i] == 0:
        fac[i] = i
        pr.append(i)
    for p in pr:
        if p > fac[i] or i * p > 10000000:
            break
        fac[i * p] = p

# Random numbers are likely 
ch_random = 0.5
ch_prime = 0.25

def gen_number(upper):
    if random.random() < ch_random:
        return random.randint(1, upper)
    elif random.random() < ch_prime / (1 - ch_random):
        # Choose a prime in the range.
        # upper = largest prime <= upper
        lo = 0
        hi = len(pr)
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if pr[mid] < upper:
                lo = mid
            else:
                hi = mid
        index = random.randint(1, lo-1)
        return pr[index]
    else:
        # Choose a random number by repeatedly multiplying by small primes.
        choices = pr[:15]
        cur = 1
        fails = 0
        while cur <= upper and fails < 5:
            m = random.choice(choices)
            if cur * m <= upper:
                cur *= m
                fails = -1
            fails += 1
        return cur

with open("tests/1.in", "w") as f:
    f.write("""\
2
6
16
""")

N_EASY = 2
N_MEDIUM = 3
N_HARD = 5
for x in range(2, N_EASY+1):
    t = random.randint(50000, 100000)
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{t}\n")
        for _ in range(t):
            n = gen_number(100)
            f.write(f"{n}\n")
for x in range(N_EASY+1, N_EASY+N_MEDIUM+1):
    t = random.randint(50000, 100000)
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{t}\n")
        for _ in range(t):
            n = gen_number(100000)
            f.write(f"{n}\n")
for x in range(N_EASY+N_MEDIUM+1, N_EASY+N_MEDIUM+N_HARD+1):
    t = random.randint(50000, 100000)
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{t}\n")
        for _ in range(t):
            n = gen_number(2000000)
            f.write(f"{n}\n")
