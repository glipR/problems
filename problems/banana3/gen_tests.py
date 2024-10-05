import random

# Sample
with open("tests/1.in", "w") as f:
    f.write("""4 3
15
8
31
42
1 1000
2 10
5 20""")

for x in range(2, 16):
    with open(f"tests/{x}.in", "w") as f:
        n = random.randint(1, 10**3)
        v = random.randint(1, 30)
        f.write(f"{n} {v}\n")
        for _ in range(n):
            a = random.randint(1, 10**2)
            f.write(f"{a}\n")
        for _ in range(v):
            if random.random() < 0.1:
                a_j = random.randint(1, 10**6)
            else:
                a_j = random.randint(1, 10**2)
            ratio = 10 * (0.8 + random.random() * 0.4)
            c = int(a_j * ratio)
            f.write(f"{a_j} {c}\n")

