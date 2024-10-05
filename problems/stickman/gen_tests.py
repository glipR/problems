import random

MAX_AREA = 1000000
MAX_VAL = 1000

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
5 4
1 2 W W
10 1 W G
W W W W
W 4 1 S
3 5 4 W
*XXX
*XX*
XXXX
X**X
*XXX
""")

# Many different paths
write_test(1, """\
5 5
S 5 5 5 5
5 5 5 5 5
5 5 G 5 5
5 5 5 5 5
5 5 5 5 5
XXXXX
***XX
XXX**
XX***
XX***
""")

# Only one path with no coins
write_test(1, """\
10 10
W 1 1 1 1 1 1 1 1 G
W W W W W W W 1 W W
1 1 1 1 1 1 W 1 1 1
W W W W W 1 1 W W W
1 1 1 1 1 1 W 1 1 1
W W W W W W 1 1 W W
1 1 1 1 1 1 1 W 1 1
W W W W W W W W 1 W
1 1 1 1 1 1 1 1 1 W
S W W W W W W W W W
X******XXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
""")

# Big lines
write_test(1, """\
5 1
5
S
W
G
5
X
*
X
X
*
""")

write_test(1, """\
1 5
5 S W G 5
X*XX*
""")

# Large test with many possible paths
n = random.randint(MAX_AREA//10000, MAX_AREA//100)
m = random.randint(MAX_AREA//n//2, MAX_AREA//n)
grid = [["W" if min(x, y) == 0 or x == n-1 or y == m-1 else 5 for y in range(m)] for x in range(n)]
coins = ["".join(["X" if min(x, y) == 0 or x == n-1 or y == m-1 else random.choice("X*") for y in range(m)]) for x in range(n)]
grid[1][1] = "S"
grid[n//2][m//2] = "G"
grid_text = "\n".join(" ".join(map(str,row)) for row in grid)
coin_text = "\n".join(coins)
write_test(1, f"""\
{n} {m}
{grid_text}
{coin_text}
""")

# Large test with random sticky values
n = random.randint(MAX_AREA//10000, MAX_AREA//100)
m = random.randint(MAX_AREA//n//2, MAX_AREA//n)
grid = [[random.randint(1, MAX_VAL) for y in range(m)] for x in range(n)]
grid[1][1] = "S"
grid[n//2][m//2] = "G"
coins = ["".join("X" for _ in range(m)) for _ in range(n)]
grid_text = "\n".join(" ".join(map(str,row)) for row in grid)
coin_text = "\n".join(coins)
write_test(1, f"""\
{n} {m}
{grid_text}
{coin_text}
""")
