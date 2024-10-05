import random

test_set_num = {}
def write_test(set_num, i, j):
    if type(set_num) == list:
        for num in set_num:
            write_test(num, i, j)
        return
    if set_num not in test_set_num:
        test_set_num[set_num] = 0
    test_set_num[set_num] += 1
    with open(f"tests/{set_num}_{test_set_num[set_num]}.in", "w") as f:
        f.write(str(i) + " " + str(j))

# Small cases
write_test(1, 1, 2)
write_test(1, 1, 3)
write_test(1, 2, 2)

# Boundary cases
write_test(1, 1<<3, 3)
write_test(1, 1<<5, 3)
write_test(1, 1<<8, 3)

write_test(1, 1<<10, 10)
write_test(1, 1<<10, 16)
write_test(1, 1<<16, 10)

# Large cases

for _ in range(30):
    write_test(1, 1 << random.randint(1, 40), random.randint(2, 5*int(pow(10, 4))))
