import random

# Sample
with open("tests/1.in", "w") as f:
    f.write("""\
3 7
2 5 squaw
0 3 breepip
5 2 keeki
""")

# 1 bird
with open("tests/2.in", "w") as f:
    f.write("""\
1 5
0 3 a
""")

# Overlapping multiples
with open("tests/3.in", "w") as f:
    f.write("""\
4 20
0 4 a
2 4 b
2 4 c
2 8 d
""")

# Duplicate strings
with open("tests/4.in", "w") as f:
    f.write("""\
4 20
0 4 a
0 4 a
1 4 ab
3 8 ab
""")

# Limit test
MAX_BIRDS = 50
MAX_SOUNDS = 500
MAX_START = 100
MAX_JUMP = 100

alph = "abcdefghijklmnopqrstuvwxyz"

def random_name():
    length = random.randint(5, 25)
    return "".join(random.choice(alph) for _ in range(length))

def make_test_case(x, nbirds, nsounds):
    lines = "\n".join(
        f"{random.randint(0, MAX_START)} {random.randint(1, MAX_JUMP)} {random_name()}"
        for _ in range(nbirds)
    )
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{nbirds} {nsounds}\n{lines}")

make_test_case(5, MAX_BIRDS, MAX_SOUNDS)

for x in range(6, 16):
    nbirds = random.randint(MAX_BIRDS//2, MAX_BIRDS)
    nsounds = random.randint(MAX_SOUNDS//2, MAX_SOUNDS)

    make_test_case(x, nbirds, nsounds)
