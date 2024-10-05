import random

with open("tests/1.in", "w") as f:
    f.write("xooxooxo\n4\n")

for x in range(2, 16):
    with open(f"tests/{x}.in", "w") as f:
        res = "".join([random.choice("xo") for _ in range(8)])
        pos = str(random.randint(1, 8))
        f.write(res + "\n" + pos + "\n")
