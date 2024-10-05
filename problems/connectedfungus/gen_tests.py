with open("tests/1.in", "w") as f:
    f.write("""\
2
3 6
1 2 1
1 3 1
2 4 2
2 5 1
3 6 4
4 5
1 2 1
2 3 2
3 4 2
4 5 1
""")

import random
single_test = 0.5
MAXN = 100000
MAXDEPTH = 6

def random_tree(n_nodes, depth, root=1):
    if depth == 1:
        return []
    if n_nodes == 1:
        return []
    # Decide on a branching factor.
    minbranching = 1
    maxbranching = n_nodes - 1
    optimalbranching = max(1, pow(n_nodes, 1/(depth - 1)))
    branching_factor = int((random.randint(minbranching, maxbranching) + optimalbranching) / 2)
    if depth == 2:
        branching_factor = n_nodes-1
    remaining_nodes = n_nodes - 1 - branching_factor
    cut = [0] + [random.randint(0, remaining_nodes) for _ in range(branching_factor-1)] + [remaining_nodes]
    cut.sort()
    tree_nodes = [cut[x+1]-cut[x] for x in range(branching_factor)]
    cur = []
    r = root + 1
    for i in range(branching_factor):
        cur.append((root, r))
        cur.extend(random_tree(tree_nodes[i]+1, depth-1, r))
        r += tree_nodes[i]+1
    return cur

def thick_tree(n_nodes, depth, fixed_branching, root=1):
    if depth == 1:
        return []
    if n_nodes == 1:
        return []
    # Decide on a branching factor.
    fixed_branching = min(fixed_branching, n_nodes-1)
    if depth == 2:
        fixed_branching = n_nodes-1
    remaining_nodes = n_nodes - 1 - fixed_branching
    cut = [0] + [random.randint(0, remaining_nodes) for _ in range(fixed_branching-1)] + [remaining_nodes]
    cut.sort()
    tree_nodes = [cut[x+1]-cut[x] for x in range(fixed_branching)]
    cur = []
    r = root + 1
    for i in range(fixed_branching):
        cur.append((root, r))
        cur.extend(random_tree(tree_nodes[i]+1, depth-1, r))
        r += tree_nodes[i]+1
    return cur


for x in range(2, 10):
    with open(f"tests/{x}.in", "w") as f:
        if random.random() < single_test:
            tests = 1
        else:
            tests = random.randint(1, 100)
        total_n = random.randint(MAXN//2, MAXN)
        splits = [0] + [random.randint(1, total_n-1) for _ in range(tests-1)] + [total_n]
        splits.sort()
        cases = [splits[x+1] - splits[x] for x in range(tests) if splits[x+1] - splits[x] > 0]
        f.write(f"{len(cases)}\n")
        for n in cases:
            rd_tree = random_tree(n, MAXDEPTH)
            # x should be large enough to force some components to form.
            x_pow = 4 + 5 * random.random()
            x = int(pow(10, x_pow))
            transmissibilities = [int(pow(10, random.random() * 9)) for _ in range(len(rd_tree))]
            f.write(f"{x} {n}\n")
            for i in range(len(rd_tree)):
                f.write(f"{rd_tree[i][0]} {rd_tree[i][1]} {transmissibilities[i]}\n")

# One bad case: very flat
with open(f"tests/10.in", "w") as f:
    f.write("1\n")
    f.write(f"2000 {MAXN}\n")
    for x in range(2, MAXN+1):
        f.write(f"1 {x} {random.randint(1, 2500)}\n")
# One bad case: very long.
with open(f"tests/11.in", "w") as f:
    f.write("1\n")
    f.write(f"2000 {MAXN}\n")
    # 4 fixed branching ensures that many nodes at the bottom.
    rd_tree = thick_tree(MAXN, MAXDEPTH, 4)
    # x should be large enough to force some components to form.
    x_pow = 4 + 5 * random.random()
    x = int(pow(10, x_pow))
    transmissibilities = [int(pow(10, random.random() * 9)) for _ in range(len(rd_tree))]
    for i in range(len(rd_tree)):
        f.write(f"{rd_tree[i][0]} {rd_tree[i][1]} {transmissibilities[i]}\n")
