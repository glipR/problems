# Final complexity: O(N*N*Depth)
# Make sure, for problem given, Depth <= 2N, meaning N^3 feasible.
# Also include test cases where this depth is maximal and the tree is complex.

n = int(input())

grid = [input() for _ in range(n)]

values = [list(map(int, input().split())) for _ in range(n)]

translation = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

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

# print(node_mapping)
# print(values_sizes)
# print(depth)

# Now we can define our DP
# DP[l][i] = Best possible stock boost given that we have access to subtree i, as well as the first l nodes above the subtree.
DP = [[None for _ in range(nodes)] for _ in range(depth)]
# First, precompute the value size of the first l characters above i.
precomp_value_size = [[None for _ in range(nodes)] for _ in range(depth)]

for i in range(nodes):
    precomp_value_size[0][i] = (0, 0)
    c = i
    for l in range(1, depth):
        if c == OUTSIDE:
            precomp_value_size[l][i] = (precomp_value_size[l-1][i])
            continue
        c = adj[c][0]
        precomp_value_size[l][i] = (precomp_value_size[l-1][i][0] + values_sizes[c][0], precomp_value_size[l-1][i][1] + values_sizes[c][1])

def solve(l, i):
    if DP[l][i] != None:
        return DP[l][i]
    if len(back_adj[i]) == 0:
        value, size = values_sizes[i][0] + precomp_value_size[l][i][0], values_sizes[i][1] + precomp_value_size[l][i][1]
        DP[l][i] = value * size
        return DP[l][i]
    # Otherwise, loop over the index that gets the multiplier.
    extra = [solve(l+1, j) for j in back_adj[i]]
    normal = [solve(0, j) for j in back_adj[i]]
    extra_sum = sum(extra)
    normal_sum = sum(normal)
    cur_max = -1
    for x in range(len(back_adj[i])):
        cur_max = max(cur_max, extra[x] + normal_sum - normal[x])
    DP[l][i] = cur_max
    return cur_max

def backtrack(l, i):
    if len(back_adj[i]) == 0:
        return [i]
    # Otherwise, loop over the index that gets the multiplier.
    extra = [solve(l+1, j) for j in back_adj[i]]
    normal = [solve(0, j) for j in back_adj[i]]
    extra_sum = sum(extra)
    normal_sum = sum(normal)
    for x in range(len(back_adj[i])):
        cur_max = extra[x] + normal_sum - normal[x]
        if cur_max == DP[l][i]:
            res = backtrack(l+1, back_adj[i][x])
            for y in range(len(back_adj[i])):
                if y != x:
                    res.extend(backtrack(0, back_adj[i][y]))
            return res

longest = solve(0, OUTSIDE)

# print(longest)
starts = [back[x] for x in backtrack(0, OUTSIDE)]
# print(starts)
print(len(starts))
for y, x in starts:
    print(y, x)
