with open("tests/1.in", "w") as f:
    f.write("""\
4 4 1
0 1
-1 3
1 3
3 2
""")

import random

x_bound = 10**7
y_bound = 10**7

for x in range(2, 11):
    with open(f"tests/{x}.in", "w") as f:
        n = random.randint(140, 300)
        h = random.randint(2, y_bound)
        points = [(random.randint(-x_bound, x_bound), random.randint(1, h-1)) for _ in range(n)]
        b = random.randint(1, 100)
        f.write(f"{h} {n} {b}\n")
        for p in points:
            f.write(f"{p[0]} {p[1]}\n")

with open(f"tests/11.in", "w") as f:
    f.write("10 0 2\n")
