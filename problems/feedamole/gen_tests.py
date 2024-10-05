import random

with open("tests/0_1.in", "w") as f:
    f.write("""3 2 5
0
1 1 1
1 1 2
2 3 1 3 2
1 3 1
""")

with open("tests/1_1.in", "w") as f:
    f.write("""3 1 4
2 1 1 3 1
1 1 1
1 2 1
1 3 1
""")

with open("tests/1_2.in", "w") as f:
    f.write("""3 3 5
3 1 1 2 2 3 3
2 1 2 3 2
1 2 2
3 2 1 1 2 3 2
2 1 1 1 3
""")

with open("tests/1_3.in", "w") as f:
    f.write("""1 1 1
0
""")

SMALL_RD_SPAWN_CHANCE = 1/5
for testno in range(4, 11):
    w, h = random.randint(1, 3), random.randint(1, 3)
    t = random.randint(1, 5)
    spawns = []
    for i in range(t):
        spawns.append([])
        for x in range(1, w+1):
            for y in range(1, h+1):
                if random.random() < SMALL_RD_SPAWN_CHANCE:
                    spawns[-1].append((x, y))
    with open(f"tests/1_{testno}.in", "w") as f:
        f.write(f"{w} {h} {t}\n")
        for i in range(t):
            f.write(str(len(spawns[i])))
            if len(spawns[i]):
                f.write(" " + " ".join(map(lambda spawn: f"{spawn[0]} {spawn[1]}", spawns[i])) + "\n")
            else:
                f.write("\n")

with open("tests/2_1.in", "w") as f:
    f.write("""40 1 5
2 40 1 1 1
1 39 1
3 40 1 38 1 3 1
0
1 36 1
""")

with open("tests/2_2.in", "w") as f:
    f.write("""40 40 1
0
""")

with open("tests/2_3.in", "w") as f:
    f.write("""1 1 1
1 1 1
""")

LARGE_RD_SPAWN_CHANCE = 1/10
for testno in range(4, 11):
    w, h = random.randint(1, 40), random.randint(1, 40)
    t = random.randint(1, 100)
    spawns = []
    for i in range(t):
        spawns.append([])
        for x in range(1, w+1):
            for y in range(1, h+1):
                if random.random() < LARGE_RD_SPAWN_CHANCE:
                    spawns[-1].append((x, y))
    with open(f"tests/2_{testno}.in", "w") as f:
        f.write(f"{w} {h} {t}\n")
        for i in range(t):
            f.write(str(len(spawns[i])))
            if len(spawns[i]):
                f.write(" " + " ".join(map(lambda spawn: f"{spawn[0]} {spawn[1]}", spawns[i])) + "\n")
            else:
                f.write("\n")
