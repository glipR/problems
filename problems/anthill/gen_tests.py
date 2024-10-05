import random
from typing import Union

with open("tests/0_1.in", "w") as f:
    f.write("""8
1 2 4
2 3 2
2 4 3
4 5 3
4 6 2
6 7 2
6 8 1
""")


# Some edge cases
with open("tests/1_1.in", "w") as f:
    # Full Binary tree
    distances = list(range(1, 20000))
    random.shuffle(distances)

    n = 9999

    lines = []
    for i in range(2, n + 1):
        lines.append(f"{i//2} {i} {distances[i]}\n")
    f.write(f"{n}\n")
    f.writelines(lines)

with open("tests/1_2.in", "w") as f:
    # Long Path
    distances = list(range(1, 20000))
    random.shuffle(distances)

    n = 9999

    lines = []
    for i in range(2, n+1):
        if i % 2 == 0:
            lines.append(f"{i} {i-1} {distances[i]}\n")
        else:
            lines.append(f"{i-2} {i} {distances[i]}\n")
    f.write(f"{n}\n")
    f.writelines(lines)

from dataclasses import dataclass, field

@dataclass
class Node:
    parent: Union[None, 'Node']
    value: int
    children: list['Node'] = field(default_factory=list)

for x in range(3, 11):
    with open(f"tests/1_{x}.in", "w") as f:
        n = random.randint(5000, 10000)
        distances = list(range(1, 20000))
        random.shuffle(distances)

        tree = Node(None, 1)
        remaining_nodes = n-1
        cur_tree_val = 2
        def build_tree(cur_node: Node):
            global remaining_nodes, cur_tree_val
            # First, decide how many children this node has.
            if remaining_nodes == 0:
                return
            n_children = remaining_nodes - 1
            # We never want there to be 1 remaining node.
            while n_children == remaining_nodes - 1:
                n_children = random.randint(2, remaining_nodes)

            remaining_nodes -= n_children
            for _ in range(n_children):
                cur_node.children.append(Node(cur_node, cur_tree_val))
                cur_tree_val += 1
                # This strat always places the entire subtree on on subpath but idm
                # Tree generation without 2 degree nodes is a pain.
                build_tree(cur_node.children[-1])

        build_tree(tree)

        def build_edges(root: Node, edge_list: list):
            for child in root.children:
                edge_list.append(f"{child.value} {root.value} {distances[child.value]}\n")
                build_edges(child, edge_list)

        edges = []
        build_edges(tree, edges)

        f.write(f"{n}\n")
        f.writelines(edges)
