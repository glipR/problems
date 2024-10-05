import random

test_set_num = {}
def write_test(set_num, text):
    if type(set_num) == list:
        for num in set_num:
            write_test(num, i, j)
        return
    if set_num not in test_set_num:
        test_set_num[set_num] = 0
    test_set_num[set_num] += 1
    with open(f"tests/{set_num}_{test_set_num[set_num]}.in", "w") as f:
        f.write(text)

write_test(1, f"{1} {1}")
write_test(1, f"{2} {1}")
write_test(1, f"{2} {3}")
write_test(1, f"{5} {5}")
write_test(1, f"{4} {3}")
write_test(1, f"{12} {10}")

# Boundary - very large difference but still same floorlog.
write_test(1, f"{1<<40} {(1<<40) + (1<<38) + (1<<37)}")
write_test(1, f"{1<<40} {(1<<41) - 1}")

# Large random tests
for _ in range(5):
    write_test(1, f"{random.randint(1, 1e18)} {random.randint(1, 1e18)}")
