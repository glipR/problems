import random

with open("tests/1.in", "w") as f:
    f.write("""\
11 8
0 1 1 0 1 1 1 0 1 0 0
0 0 1 1 1 1 1 0
0.2 0.8 0 0 1 0.5 0.5 0.5""")

MAXN = 200000
MAXM = 0.8
MAX_REQUIREMENTS = 5
MIN_PROB = 0.1
MAX_PROB = 0.9

# Random generation
for case in range(2, 11):
    with open(f"tests/{case}.in", "w") as f:
        n = random.randint(MAXN//4, MAXN)
        m = random.randint(1, int(MAXM * n))
        original_string = [random.choice("01") for _ in range(n)]
        mutated = [random.choice("01") for _ in range(m)]
        probs = [f"{MIN_PROB + random.random() * (MAX_PROB - MIN_PROB):.3f}" for _ in range(m)]
        total_requirements = random.randint(0, MAX_REQUIREMENTS)
        requirement_offset = random.randint(0, n-1)
        for _ in range(total_requirements):
            idx = random.randint(0, m-1)
            l_idx = (idx + requirement_offset) % n
            probs[idx] = "1" if (original_string[l_idx] != mutated[idx]) else "0"
        f.write(f"{n} {m}\n")
        f.write(" ".join(original_string) + "\n")
        f.write(" ".join(mutated) + "\n")
        f.write(" ".join(probs) + "\n")



