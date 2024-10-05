n = int(input())

adj_list = [[] for _ in range(n)]
par = [None]*n

roads = []
for x in range(n-1):
    i, j, d = list(map(int, input().split()))
    adj_list[i-1].append((j-1, d, x))
    adj_list[j-1].append((i-1, d, x))
    roads.append((i-1, j-1, d))

def dfs(root):
    for child, distance, idx in adj_list[root]:
        if child == par[root]: continue
        par[child] = root
        dfs(child)

dfs(0)


d = [[float("inf") for _ in range(n)] for _ in range(n)]
inbetweens = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    d[i][i] = 0
    inbetweens[i][i] = []
    for j, dist, x in adj_list[i]:
        d[i][j] = dist
        inbetweens[i][j] = [x]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if d[i][j] + d[j][k] < d[i][k]:
                d[i][k] = d[i][j] + d[j][k]
                inbetweens[i][k] = inbetweens[i][j] + inbetweens[j][k]

road_index = int(input()) - 1

total = 0
for i in range(n):
    for j in range(n):
        if road_index in inbetweens[i][j]:
            total += d[i][j]
# Double counted
print(total // 2)
