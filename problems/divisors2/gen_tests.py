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
5_1
""")

write_test(1, f"""\
2_1
""")

write_test(1, f"""\
5_5
""")

write_test(1, f"""\
1_1
""")

# Large cases

for _ in range(5):
    i_pow = random.randint(1, 11)
    i = random.randint(pow(10, i_pow-1), pow(10, i_pow))
    j = random.randint(1, 1e11 // i)
    write_test(1, f"{i}_{j}")
