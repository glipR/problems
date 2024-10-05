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
write_test(1, 0)
write_test(1, 1)
write_test(1, 2)

# Boundary cases - first mod
write_test(1, 42)
write_test(1, 43)
write_test(1, 44)
write_test(1, 45)

# Large cases

write_test(1, int(pow(10, 17) + random.randint(0, 9*pow(10, 17))))
write_test(1, int(pow(10, 17) + random.randint(0, 9*pow(10, 17))))
write_test(1, int(pow(10, 17) + random.randint(0, 9*pow(10, 17))))
