import random

test_set_num = {}
def write_test(set_num, contents):
    if type(set_num) == list:
        for num in set_num:
            write_test(num, contents)
        return
    if set_num not in test_set_num:
        test_set_num[set_num] = 0
    test_set_num[set_num] += 1
    with open(f"tests/{set_num}_{test_set_num[set_num]}.in", "w") as f:
        f.write(str(contents))

# Small cases
write_test(1, f"""\
6
1_1 2_4 1_5 5_1 3_2 2_3
""")

write_test(1, f"""\
1
3_1
""")

write_test(1, f"""\
3
1_1 1_2 2_1
""")

write_test(1, f"""\
3
4_3 5_2 2_5
""")

# Large cases

for _ in range(2):
    n_vals = random.randint(3*pow(10, 4), 10*pow(10, 4))
    point_set = set()
    while len(point_set) < n_vals:
        point_set.add(f"{random.randint(1, 1e3)}_{random.randint(1, 1e2)}")
    write_test(1, f"{n_vals}\n{' '.join(point_set)}")

for _ in range(5):
    n_vals = random.randint(3*pow(10, 4), 10*pow(10, 4))
    point_set = set()
    while len(point_set) < n_vals:
        point_set.add(f"{random.randint(1, 1e9)}_{random.randint(1, 1e9)}")
    write_test(1, f"{n_vals}\n{' '.join(point_set)}")
