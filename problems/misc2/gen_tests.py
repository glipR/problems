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

def random_tree(n):
    parents = [random.randint(0, i-1) if i > 0 else -1 for i in range(n)]
    weights = [random.randint(1, 1e3) for i in range(n)]
    return parents, weights

def print_tree(parents, weights):
    # Don't have all edges be up the tree.
    order = [random.randint(0, 1) for _ in range(len(parents))]
    # Don't have 1 be the root always
    remapping = list(range(1, len(parents)+1))
    random.shuffle(remapping)
    roads = [(remapping[i], remapping[parents[i]], weights[i]) for i in range(1, len(parents))]
    road_str = "\n".join(map(lambda x: f"{x[1][order[x[0]]]} {x[1][1 - order[x[0]]]} {x[1][2]}", enumerate(roads)))
    return f"{len(parents)}\n{road_str}"

# Statement example
parents = [-1, 0, 1, 2]
weights = [-1, 1, 3, 4]
write_test(0, f"{print_tree(parents, weights)}\n2")

# Edge cases - leaves
write_test(1, f"{print_tree(parents, weights)}\n1")
write_test(1, f"{print_tree(parents, weights)}\n3")

# Simple case that isn't a path
parents = [-1, 0, 0, 0, 2, 2]
weights = [-1, 3, 4, 1, 2, 5]
# A non-leaf
write_test(1, f"{print_tree(parents, weights)}\n2")
# A leaf
write_test(1, f"{print_tree(parents, weights)}\n4")

# A star
parents = [-1, 0, 1, 1, 1, 1, 1]
weights = [-1, 5, 4, 4, 5, 5, 3]
write_test(1, f"{print_tree(parents, weights)}\n1")
write_test(1, f"{print_tree(parents, weights)}\n2")


# Larger random cases.
for _ in range(5):
    parents, weights = random_tree(random.randint(1e5, 5e5))
    write_test(2, f"{print_tree(parents, weights)}\n{random.randint(1, len(parents)-1)}")
