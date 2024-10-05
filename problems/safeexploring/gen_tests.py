from noise import snoise2
import random

with open("tests/1.in", "w") as f:
    f.write("""\
3 2 3
1 4
3 6
2 1
1 1 2
2 1 2
2 3 1
""")

octaves = 1
freq = 16.0 * octaves

MAXQ = 10

for i in range(2, 6):
    with open(f"tests/{i}.in", "w") as f:
        n, m = random.randint(256, 500), random.randint(256, 500)
        q = random.randint(MAXQ//2, MAXQ)
        print(n, m, q, file=f)
        for y in range(n):
            for x in range(m):
                f.write(str(int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)) + (" " if x != m - 1 else "\n"))
        # Generate queries
        for _ in range(q):
            print(random.randint(1, m), random.randint(1, n), random.randint(2, 10), file=f)

MAXQ = 1000

for i in range(6, 11):
    with open(f"tests/{i}.in", "w") as f:
        n, m = random.randint(256, 500), random.randint(256, 500)
        q = random.randint(MAXQ//2, MAXQ)
        print(n, m, q, file=f)
        for y in range(n):
            for x in range(m):
                f.write(str(int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)) + (" " if x != m - 1 else "\n"))
        # Generate queries
        for _ in range(q):
            print(random.randint(1, m), random.randint(1, n), random.randint(2, 10), file=f)

MAXQ = 100000

for i in range(11, 21):
    with open(f"tests/{i}.in", "w") as f:
        n, m = random.randint(256, 500), random.randint(256, 500)
        q = random.randint(MAXQ//2, MAXQ)
        print(n, m, q, file=f)
        for y in range(n):
            for x in range(m):
                f.write(str(int(snoise2(x / freq, y / freq, octaves) * 127.0 + 128.0)) + (" " if x != m - 1 else "\n"))
        # Generate queries
        for _ in range(q):
            print(random.randint(1, m), random.randint(1, n), random.randint(2, 10), file=f)
