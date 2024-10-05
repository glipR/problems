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
        f.write(contents)

# Sample case.
write_test(0, """\
1 4 5
5 8 3 6
1 0
1 1 8
2 1 6
4 0
5 0
""")

# Extreme - day 0 and harvesting from initial
write_test([1, 2], """\
1 4 5
5 8 3 6
0 0
0 0
0 1 5
0 0
0 0
""")

# Extreme - day 0 and harvesting everything
write_test([1, 2], """\
1 1 3
5
0 0
0 1 5
1 0
""")

# Extreme = day 0 -> day 10^9
write_test([1, 2], """\
10 2 4
5 5
0 0
500000000 1 10
1000000000 0
1000000000 0
""")

# Random tests
def gen_random(set_num, easy):
    if easy:
        max_poppies = 100
        max_events = 100
    else:
        max_poppies = pow(10, 6)
        max_events = pow(10, 6)

    growth = random.randint(1, 10)
    n_initial = random.randint(1, max_poppies)
    n_events = random.randint(max_events/2, max_events)

    poppies = [random.randint(0, pow(10, 9)) for _ in range(n_initial)]
    event_days = [random.randint(0, pow(10, 9)) for _ in range(n_events)]
    event_days.sort()
    events = []
    cur_poppies = n_initial
    n_harvest = 0
    for i in range(n_events):
        if cur_poppies == 0:
            rand = 0
        else:
            rand = random.random()
        if rand < (0.5 if easy else 0.99) or n_harvest >= 2*pow(10, 4):
            # place a poppy
            events.append(f"{event_days[i]} {1} {random.randint(0, pow(10, 9))}")
            cur_poppies += 1
        else:
            events.append(f"{event_days[i]} {0}")
            cur_poppies -= 1
            n_harvest += 1

    newline = "\n"
    contents = f"""\
{growth} {n_initial} {n_events}
{" ".join(map(str, poppies))}
{newline.join(events)}
"""
    write_test(set_num, contents)

for _ in range(5):
    gen_random(1, True)

for _ in range(5):
    gen_random(2, False)
