TEST_SETS = [
    (5, 300, 1<<10),
    (10, 500, 1<<10),
    (10, 5000, 1<<15),
    (100, 20000, 1<<40)
]

N_INDIV = 10

for set_num in range(1, len(TEST_SETS)+1):
    for ind in range(1, N_INDIV+1):
        with open(f"tests/{set_num}_{ind}.in", "w") as f:
            f.write(f"{TEST_SETS[set_num-1][0]} {TEST_SETS[set_num-1][1]} {TEST_SETS[set_num-1][2]}\n")
