import random

with open("tests/1.in", "w") as f:
    f.write("""\
5
1 2 1
1 3 2
2 4 3
2 5 4
""")

NRAND = 9

for x in range(2, 2 + NRAND):
    # Gen random tree
    N = random.randint(2 * 10**5, 10**6)
    nodes = list(range(1, N+1))
    random.shuffle(nodes)
    parent = [nodes[random.randint(0, y-1)] for y in range(1, N)]
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{N}\n")
        for i, p in enumerate(parent):
            f.write(f"{nodes[i+1]} {p} {random.randint(0, 10**9)}\n")

# Tricky cases
with open(f"tests/{2+NRAND}.in", "w") as f:
    N = 10**6
    edges = [(x, x+1, random.randint(10**8, 10**9)) for x in range(1, N)]
    f.write(f"{N}\n")
    for a, b, c in edges:
        f.write(f"{a} {b} {c}\n")

with open(f"tests/{3+NRAND}.in", "w") as f:
    N = 10**6
    edges = [(1, x, random.randint(10**8, 10**9)) for x in range(2, N+1)]
    f.write(f"{N}\n")
    for a, b, c in edges:
        f.write(f"{a} {b} {c}\n")


