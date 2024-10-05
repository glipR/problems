n = int(input())

adj_list = [[] for _ in range(n)]
par = [None]*n

roads = []
for i in range(n-1):
    i, j, d = list(map(int, input().split()))
    adj_list[i-1].append((j-1, d))
    adj_list[j-1].append((i-1, d))
    roads.append((i-1, j-1, d))

def dfs(root):
    for child, distance in adj_list[root]:
        if child == par[root]: continue
        par[child] = root
        dfs(child)

dfs(0)

_num_paths_below = [None]*n
_num_paths_above = [None]*n
_sum_paths_below = [None]*n
_sum_paths_above = [None]*n

def num_paths_below(i):
    if _num_paths_below[i] != None:
        return _num_paths_below[i]
    cur = 1
    for j, distance in adj_list[i]:
        if par[i] == j: continue
        cur += num_paths_below(j)
    _num_paths_below[i] = cur
    return cur

def sum_paths_below(i):
    if _sum_paths_below[i] != None:
        return _sum_paths_below[i]
    cur = 0
    for j, distance in adj_list[i]:
        if par[i] == j: continue
        cur += sum_paths_below(j) + distance * num_paths_below(j)
    _sum_paths_below[i] = cur
    return cur

def num_paths_above(i):
    if _num_paths_above[i] != None:
        return _num_paths_above[i]
    if par[i] == None:
        return 1
    cur = num_paths_above(par[i]) + 1
    for child, distance in adj_list[par[i]]:
        if child == i: continue
        if child == par[par[i]]: continue
        cur += num_paths_below(child)
    _num_paths_above[i] = cur
    return cur

def sum_paths_above(i):
    if _sum_paths_above[i] != None:
        return _sum_paths_above[i]
    if par[i] == None:
        return 0
    for child, distance in adj_list[par[i]]:
        if child == i: par_dist = distance
    cur = sum_paths_above(par[i]) + par_dist * num_paths_above(par[i])
    for child, distance in adj_list[par[i]]:
        if child == i: continue
        if child == par[par[i]]: continue
        cur += sum_paths_below(child) + (par_dist + distance) * num_paths_below(child)
    _sum_paths_above[i] = cur
    return cur

road_index = int(input())

rx, ry, road_distance = roads[road_index - 1]
if par[rx] == ry: rx, ry = ry, rx
# Now, par[ry] = rx.

sum_x_size = sum_paths_above(rx)
for child, distance in adj_list[rx]:
    if child == ry: continue
    if child == par[rx]: continue
    sum_x_size += sum_paths_below(child) + distance * num_paths_below(child)

sum_y_size = sum_paths_below(ry)

num_x_size = num_paths_above(rx)
for child, distance in adj_list[rx]:
    if child == ry: continue
    if child == par[rx]: continue
    num_x_size += num_paths_below(child)

num_y_size = num_paths_below(ry)

total_productivity_lost = sum_x_size * num_y_size + sum_y_size * num_x_size + road_distance * num_x_size * num_y_size
print(total_productivity_lost)

