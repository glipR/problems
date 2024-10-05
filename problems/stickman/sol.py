import heapq

n, m = list(map(int, input().split()))
grid = [
    list(input().split())
    for _ in range(n)
]
coin = [input() for _ in range(n)]

start = None
end = None
for x in range(n):
    for y in range(m):
        if grid[x][y] not in "SGW":
            grid[x][y] = int(grid[x][y])
            if coin[x][y] == "*":
                grid[x][y] -= 1 / (n*m + 1)
        if grid[x][y] == "S":
            start = (x, y)
        if grid[x][y] == "G":
            end = (x, y)

expanded = set()
parent = {}
queue = []
heapq.heapify(queue)
heapq.heappush(queue, (0, start, None))

while queue:
    cur_dist, node, par = heapq.heappop(queue)
    if node in expanded:
        continue
    expanded.add(node)
    parent[node] = par
    for (ox, oy) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_pos = ((node[0] + ox) % n, (node[1] + oy) % m)
        val = grid[new_pos[0]][new_pos[1]]
        if new_pos not in expanded and val != "W":
            if val in ["S", "G"]:
                val = 0
            heapq.heappush(queue, (cur_dist + val, new_pos, node))


moves = []
cur_node = end
while cur_node != start:
    par = parent[cur_node]
    if par[0] != cur_node[0] and (par[0] - cur_node[0]) % n == n - 1:
        moves.append("D")
    elif par[0] != cur_node[0] and (par[0] - cur_node[0]) % n == 1:
        moves.append("U")
    elif par[1] != cur_node[1] and (par[1] - cur_node[1]) % m == m - 1:
        moves.append("R")
    elif par[1] != cur_node[1] and (par[1] - cur_node[1]) % m == 1:
        moves.append("L")
    cur_node = par
moves = moves[::-1]
print("".join(moves))
