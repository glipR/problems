import random

with open("tests/1.in", "w") as f:
    f.write("""5 4
..NP.
P....
.P...
..N..
17 14 7 20 100
13 21 100 100 100
100 12 9 100 100
100 100 10 5 1""")

with open("tests/2.in", "w") as f:
    f.write("""2 1
NP
17 14""")

with open("tests/3.in", "w") as f:
    f.write("""1 4
N
.
.
P
17
14
18
16""")



MAX_GRIDSIZE = 3 * pow(10, 4)
RESIST_RANGE = (0, pow(10, 9))

for tno in range(4, 11):
    while True:
        grid_width = min(
            random.randint(1, MAX_GRIDSIZE//2), 
            random.randint(1, MAX_GRIDSIZE//2),
            random.randint(1, MAX_GRIDSIZE//2),
            random.randint(1, MAX_GRIDSIZE//2),
        )
        grid_height = random.randint(max(MAX_GRIDSIZE // grid_width // 2, 1), MAX_GRIDSIZE // grid_width)
    
        P_chance = random.choice([0.001, 0.01, 0.1])
        N_chance = random.choice([0.0001, 0.001, 0.01])

        P_placed = False
        N_placed = False
        grid = [["." for _ in range(grid_width)] for _ in range(grid_height)]
        for y in range(grid_height):
            for x in range(grid_width):
                if random.random() < P_chance:
                    P_placed = True
                    grid[y][x] = "P"
                elif random.random() < N_chance:
                    N_placed = True
                    grid[y][x] = "N"

        if not (P_placed and N_placed):
            continue
        
        values = [[random.randint(*RESIST_RANGE) for _ in range(grid_width)] for _ in range(grid_height)]

        with open(f"tests/{tno}.in", "w") as f:
            f.write(f"{grid_width} {grid_height}\n" + "\n".join("".join(l) for l in grid) + "\n" + "\n".join(" ".join(map(str, l)) for l in values))
        break