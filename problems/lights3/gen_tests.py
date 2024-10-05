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
write_test(1, 1)
write_test(1, 3)
write_test(1, 6)
write_test(1, 10)

# Boundary cases
write_test(1, 1<<5)
write_test(1, (1<<5) - 1)
write_test(1, (1<<5) + 1)

# Large cases

write_test(1, int(pow(10, 17) + random.randint(0, 9*pow(10, 17))))
write_test(1, int(pow(10, 17) + random.randint(0, 9*pow(10, 17))))
write_test(1, int(pow(10, 17) + random.randint(0, 9*pow(10, 17))))
