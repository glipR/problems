import random

test_set_num = {}
def write_test(set_num, num):
    if type(set_num) == list:
        for num in set_num:
            write_test(num, num)
        return
    if set_num not in test_set_num:
        test_set_num[set_num] = 0
    test_set_num[set_num] += 1
    fake_coins = set()
    while len(fake_coins) < 3:
        fake_coins.add(random.randint(1, num))
    with open(f"tests/{set_num}_{test_set_num[set_num]}.in", "w") as f:
        f.write(str(num))
        f.write("\n" + " ".join(map(str, fake_coins)))

# Small cases
write_test(1, 3)
write_test(1, 4)
write_test(1, 5)
write_test(1, 6)
write_test(1, 9)
write_test(1, 13)

for _ in range(10):
    write_test(2, int(1e5))
