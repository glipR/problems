import random

test_set_num = {}
def write_test(set_num, *contents):
    if type(set_num) == list:
        for num in set_num:
            write_test(num, contents)
        return
    if set_num not in test_set_num:
        test_set_num[set_num] = 0
    test_set_num[set_num] += 1
    with open(f"tests/{set_num}_{test_set_num[set_num]}.in", "w") as f:
        f.write(" ".join(map(str, contents)))

# Small cases
write_test(1, 4, 6)
write_test(1, 6, 4)
write_test(1, 7, 5)
write_test(1, 10, 5)
write_test(1, 1, 3)
write_test(1, 3, 13)

# Large cases

write_test(1, int(pow(10, 5) + random.randint(0, 9*pow(10, 5))), int(pow(10, 5) + random.randint(0, 9*pow(10, 5))))
write_test(1, int(pow(10, 5) + random.randint(0, 9*pow(10, 5))), int(pow(10, 5) + random.randint(0, 9*pow(10, 5))))
write_test(1, int(pow(10, 5) + random.randint(0, 9*pow(10, 5))), int(pow(10, 5) + random.randint(0, 9*pow(10, 5))))
