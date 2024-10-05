import random

MAX_SIZE = 1000

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

write_test(0, """\
4
X..X
.X..
..X.
X..X
""")

write_test(1, """\
5
.....
.....
.....
.....
.....
""")

write_test(1, """\
5
XXXXX
XXXXX
XXXXX
XXXXX
XXXXX
""")

write_test(1, """\
3
X..
X..
X..
""")

write_test(1, """\
10
XXX.......
XXX.......
XXX.......
.....XXX..
.....XXX..
..XXX.....
..XXX.....
.......XXX
.......XXX
.......XXX
""")

# Size test
nl = "\n"
write_test(1, f"""\
{MAX_SIZE}
{nl.join(''.join(random.choice('.X') for _ in range(MAX_SIZE)) for _ in range(MAX_SIZE))}
""")
