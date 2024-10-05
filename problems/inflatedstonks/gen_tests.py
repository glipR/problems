import random

# Sample
with open("tests/1.in", "w") as f:
    f.write("""4
RRDL
LUDR
UULL
RRLL
4 8 2 10
1 1 1 1
1 1 1 1
6 1 1 4
""")

# Edge case: tiny.
with open("tests/2.in", "w") as f:
    f.write("""1
D
1
""")

translation = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

for tno in range(3, 11):
    MAX_N = 100
    MAX_D = 1000000
    MAX_DEPTH = lambda N: 4 * N

    while True:
        n = random.randint(1, MAX_N)

        grid = ["".join([random.choice("UDLR") for _ in range(n)]) for _ in range(n)]
        values = [[random.randint(0, MAX_D) for _ in range(n)] for _ in range(n)]

        # Check depth 
        # First, cycle finding.
        edge_mapping = {}
        counter = 1
        cycle_map = {}
        cycle_value_size = {}
        marked = [[0 for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if marked[x][y] == 0:
                    marked[x][y] = counter
                    cx, cy = x, y
                    while True:
                        dx, dy = translation[grid[cx][cy]]
                        cx, cy = cx + dx, cy + dy
                        if not (0 <= cx < n and 0 <= cy < n):
                            break
                        if marked[cx][cy] == 0:
                            marked[cx][cy] = counter
                            continue
                        if marked[cx][cy] == counter:
                            # We have found a cycle. Do another search until I find myself.
                            ax, ay = cx, cy
                            total_value = values[cx][cy]
                            total_size = 1
                            while True:
                                dx, dy = translation[grid[ax][ay]]
                                ax, ay = ax + dx, ay + dy
                                if ax == cx and ay == cy:
                                    break
                                cycle_map[(ax, ay)] = (cx, cy)
                                total_value += values[ax][ay]
                                total_size += 1
                            cycle_value_size[(cx, cy)] = (total_value, total_size)
                        # Otherwise, we found an already searched strand. No cycles here.
                        # In either case, stop the search.
                        break
                    counter += 1

        nodes = 0
        node_mapping = {}
        back = []
        for x in range(n):
            for y in range(n):
                if (x, y) in cycle_map:
                    continue
                node_mapping[(x, y)] = nodes
                back.append((x, y))
                nodes += 1
        OUTSIDE = nodes
        nodes += 1
        adj = [[] for _ in range(nodes)]
        back_adj = [[] for _ in range(nodes)]
        values_sizes = []
        for x in range(n):
            for y in range(n):
                if (x, y) in cycle_map:
                    continue
                if (x, y) in cycle_value_size:
                    values_sizes.append(cycle_value_size[(x, y)])
                    adj[node_mapping[(x, y)]].append(OUTSIDE)
                    back_adj[OUTSIDE].append(node_mapping[(x, y)])
                else:
                    values_sizes.append((values[x][y], 1))
                    dx, dy = translation[grid[x][y]]
                    cx, cy = x + dx, y + dy
                    if not (0 <= cx < n and 0 <= cy < n):
                        adj[node_mapping[(x, y)]].append(OUTSIDE)
                        back_adj[OUTSIDE].append(node_mapping[(x, y)])
                    else:
                        if (cx, cy) in cycle_map:
                            cx, cy = cycle_map[(cx, cy)]
                        adj[node_mapping[(x, y)]].append(node_mapping[(cx, cy)])
                        back_adj[node_mapping[(cx, cy)]].append(node_mapping[(x, y)])
        # OUTSIDE value + size.
        values_sizes.append((0, 0))

        # We now have a node list with adjacency list, storing cycles as a single vertex, and keeping track of the value and length of each node.
        # Start by computing the max depth of the tree.
        dist = [None] * nodes
        def rec_d(v, d=0):
            dist[v] = d
            m = d
            for u in back_adj[v]:
                m = max(rec_d(u, d+1), m)
            return m

        depth = rec_d(OUTSIDE, 0) + 1
        if depth > MAX_DEPTH(n):
            continue
        # Write the test
        grid_string = "\n".join(grid)
        value_string = "\n".join(map(lambda t: " ".join(map(str, t)), values))
        with open(f"tests/{tno}.in", "w") as f:
            f.write(str(n) + "\n" + grid_string + "\n" + value_string)
        break
