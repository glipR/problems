with open("tests/1.in", "w") as f:
    f.write("""\
2
4 3
1 8 3 7
7 3
1 2 3 6 7 9 10
""")

import random
single_chance = 0.5

EASY_N = 100
MED_N = 1000
HARD_N = 100000

maxv = 10**9

for x in range(2, 12):
    with open("tests/{}.in".format(x), "w") as f:
        if x < 5:
            n = EASY_N
        elif x < 8:
            n = MED_N
        else:
            n = HARD_N
        tests = random.randint(1, min(1000, n//2))
        if random.random() < single_chance:
            tests = 1
        total_n = random.randint(max(tests, n//2), max(tests, n))
        splits = [0] + [random.randint(0, n-tests) for _ in range(tests-1)] + [n-tests]
        splits.sort()
        amounts = [splits[y+1] - splits[y] + 1 for y in range(tests)]
        f.write(f"{tests}\n")
        for case in range(tests):
            k = random.randint(0, 10)
            f.write(f"{amounts[case]} {k}\n")
            f.write(" ".join(str(random.randint(0, maxv)) for _ in range(amounts[case])) + "\n")
