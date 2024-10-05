import random

def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a%b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

pr = []
fac = [0]*(10**6+1)
for i in range(2, 10**6+1):
    if fac[i] == 0:
        fac[i] = i
        pr.append(i)
    for p in pr:
        if p > fac[i] or i * p > 10**6:
            break
        fac[i*p] = p

def facts(n):
    res = []
    while n > 1:
        f = fac[n]
        n //= f
        res.append(f)
    return res

def gen_positions(k, reps, total_n):
    period = total_n // reps
    k_per_rep = k // reps
    spots = set()
    while len(spots) < k_per_rep:
        spots.add(random.randint(1, period))
    spots = list(sorted(list(spots)))
    all_positions = [None]*k
    for i in range(reps):
        for i2 in range(k_per_rep):
            all_positions[i*k_per_rep+i2] = spots[i2] + period * i
    return all_positions

with open("tests/1.in", "w") as f:
    f.write("""\
2
6
2 2 5
2 3 6
4 1 2 4 5
12
6 3 4 7 8 11 12
6 2 4 6 8 10 12
0
""")


single_chance = 0.5

NRAND = 9
for x in range(2, NRAND+2):
    if single_chance > random.random():
        T = 1
    else:
        T = random.randint(10, 1000)
    print(T)
    sum_k = random.randint(2*10**5, 10**6)
    partitions = [random.randint(0, sum_k) for _ in range(T-1)]
    partitions.append(0)
    partitions.append(sum_k)
    partitions.sort()
    k_vals = [partitions[x+1] - partitions[x] for x in range(len(partitions)-1)]
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{T}\n")
        for c in range(T):
            # We want N to be a factor of k_vals
            MAXK = k_vals[c]
            # Now, all 3 k_values need to share a common divisor
            # First, we pick a k_value with lots of small prime factors
            r = 1
            for p in pr[:10]:
                while r * p <= MAXK // 3:
                    if random.random() < 0.3:
                        break
                    r *= p
            # r will be our final answer (Our entire sequence will repeat r times).
            total_k_per_repeat = MAXK // r
            # Now we have to spread our k amongst r repeats, and 3 sequences.
            # We are guaranteed that total_k_per_repeat >= 3, as r < MAXK//3
            first_shelf_per_repeat = random.randint(0, total_k_per_repeat)
            second_shelf_per_repeat = random.randint(0, total_k_per_repeat-first_shelf_per_repeat)
            third_shelf_per_repeat = total_k_per_repeat - first_shelf_per_repeat - second_shelf_per_repeat
            # We can decide on some extra repetition within, if our k/repeat has some factors.
            f1 = facts(first_shelf_per_repeat)
            f2 = facts(second_shelf_per_repeat)
            f3 = facts(third_shelf_per_repeat)
            r_1 = 1
            r_2 = 1
            r_3 = 1
            for factor in f1:
                if random.random() > 0.5:
                    r_1 *= factor
            for factor in f2:
                if random.random() > 0.5:
                    r_2 *= factor
            for factor in f3:
                if random.random() > 0.5:
                    r_3 *= factor
            # Now, we want our total_n to allow for r1 * repeat, r2 * repeat and r3 * repeat repetitions. So it must divide all 3.
            min_n = lcm(lcm(r_1 * r, r_2 * r), r_3 * r)
            max_fact = 10**18 // min_n
            total_n = min_n * random.randint(max(1, max_fact//2), max_fact) 
            p1 = " ".join(list(map(str, gen_positions(first_shelf_per_repeat * r, r_1 * r, total_n))))
            p2 = " ".join(list(map(str, gen_positions(second_shelf_per_repeat * r, r_2 * r, total_n))))
            p3 = " ".join(list(map(str, gen_positions(third_shelf_per_repeat * r, r_3 * r, total_n))))
            f.write(f"{total_n}\n")
            f.write(f"{len(p1)} {p1}\n")
            f.write(f"{len(p2)} {p2}\n")
            f.write(f"{len(p3)} {p3}\n")
            assert 1 <= total_n <= 10**18
            assert 0 <= r * (first_shelf_per_repeat + second_shelf_per_repeat + third_shelf_per_repeat) <= MAXK, f"{len(p1)}, {len(p2)}, {len(p3)}, {MAXK}"
        assert sum(k_vals) <= 10**6
