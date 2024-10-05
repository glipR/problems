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
5
""")

write_test(1, f"""\
1
""")

write_test(1, f"""\
10
""")

write_test(1, f"""\
1000
""")

# Large cases

for _ in range(5):
    i_pow = random.randint(4, 11)
    i = random.randint(pow(10, i_pow-1), pow(10, i_pow))
    write_test(1, i)
