import random
# Test Set A

with open("tests/1_3.in", "w") as f:
    f.write("20 20 20\n")
    for x in range(20):
        f.write(f"{x} 19\n")

with open("tests/1_4.in", "w") as f:
    point_set = set()
    while len(point_set) < 20:
        x = random.randint(0, 99)
        y = random.randint(0, 99)
        point_set.add((x, y))

    f.write("100 100 20\n")
    for x, y in point_set:
        f.write(f"{x} {y}\n")

with open("tests/1_5.in", "w") as f:
    f.write("100 20 20\n")
    for y in range(20):
        f.write(f"50 {20-y-1}\n")

with open("tests/1_6.in", "w") as f:
    f.write("6 6 20\n")
    count = 0
    for x in range(6):
        for y in range(6):
            if ((x in [0, 5]) or (y in [0, 5])) and count < 20:
                count += 1
                f.write(f"{x} {y}\n")

with open("tests/1_7.in", "w") as f:
    f.write("10 2 3\n")
    f.write("7 1\n")
    f.write("2 0\n")
    f.write("0 1\n")

with open("tests/1_8.in", "w") as f:
    f.write("2 10 3\n")
    f.write("1 7\n")
    f.write("0 2\n")
    f.write("1 0\n")

# Test Set B
for case in range(1, 4):
    with open(f"tests/2_{case}.in", "w") as f:
        point_set = set()
        while len(point_set) < 10000:
            x = random.randint(0, 1000-1)
            y = random.randint(0, 1000-1)
            point_set.add((x, y))

        f.write("1000 1000 10000\n")
        for x, y in point_set:
            f.write(f"{x} {y}\n")

for case in range(4, 6):
    with open(f"tests/2_{case}.in", "w") as f:
        point_set = set()
        while len(point_set) < 1000:
            x = random.randint(0, 1000-1)
            y = random.randint(0, 1000-1)
            point_set.add((x, y))

        f.write("1000 1000 1000\n")
        for x, y in point_set:
            f.write(f"{x} {y}\n")



