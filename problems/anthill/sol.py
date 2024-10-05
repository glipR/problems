import sys
sys.setrecursionlimit(50000)

n = int(input())

adj_list = [[] for _ in range(n)]

for _ in range(n-1):
    a, b, d = list(map(int, input().split()))
    adj_list[a-1].append((b-1, d))
    adj_list[b-1].append((a-1, d))

par = [None] * n
def dfs(i, parent=None, par_dist=0):
    par[i] = parent, par_dist
    for child, dist in adj_list[i]:
        if child != parent:
            dfs(child, i, dist)

dfs(0)

actions = []
def generate_actions(i):
    if par[i][1]:
        actions.append(f"TUNNEL {par[i][1]}")
    for child, _dist in adj_list[i]:
        if child != par[i][0]:
            generate_actions(child)
    if par[i][1]:
        actions.append(f"BACK {par[i][1]}")

generate_actions(0)

print(len(actions))
print("\n".join(actions))
