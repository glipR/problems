import random

with open("tests/1.in", "w") as f:
    f.write("""\
7
22 9 25 13 3 19 14
""")

with open("tests/2.in", "w") as f:
    f.write("""\
1
5
""")

with open("tests/3.in", "w") as f:
    f.write("100\n" + " ".join(str(5*x) for x in range(1, 101)))

MAX_N = pow(10, 6)
MAX_V = pow(10, 9)

for tno in range(4, 11):
    n = random.randint(MAX_N//2, MAX_N)
    average_distance = random.choice([1, 2, 3])
    span = average_distance * (n-1)
    maxval = random.randint(span + 1, MAX_V)
    nums = [random.randint(maxval - span, maxval) for _ in range(n)]
    with open(f"tests/{tno}.in", "w") as f:
        f.write(f"{n}\n" + " ".join(list(map(str, nums))))
