import random
# Some particular cases:

# 1: Sample
with open("tests/1.in", "w") as f:
    f.write("""\
2
3 5
5 1
""")

# 2: 0 not possible answer
with open("tests/2.in", "w") as f:
    f.write("3\n1 1\n6 6\n9 9")

triple_chance = 0.5

# 3-20: Random.
for x in range(3, 21):
    with open(f"tests/{x}.in", "w") as f:
        t = random.randint(1, 10000)
        f.write(f"{t}\n")
        for _ in range(t):
            if random.random() < triple_chance:
                n = random.randint(1,    100)
                m = random.randint(n+1, 200)
                nums = [m*m - n*n, 2*n*m, n*n + m*m]
                del nums[random.randint(0, 2)]
                random.shuffle(nums)
                f.write(f"{nums[0]} {nums[1]}\n")
            else:
                a, b = random.randint(1, 100000), random.randint(1, 100000)
                f.write(f"{a} {b}\n")
