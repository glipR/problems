MAX_RES = pow(10, 9)

w, h = list(map(int, input().split()))
grid = [
    input()
    for _ in range(h)
]
values = [
    list(map(int, input().split()))
    for _ in range(h)
]

# BINARY SEARCH
visited = [[False for _ in range(w)] for _ in range(h)]
lo = 0
hi = MAX_RES
while hi != lo:
    mid = (hi + lo) // 2
    DFS = []
    for y in range(h):
        for x in range(w):
            visited[y][x] = grid[y][x] == "N" and values[y][x] <= mid
            if visited[y][x]:
                DFS.append((y, x))
    while DFS:
        y, x = DFS.pop()
        for a, b in [
            (y+1, x),
            (y-1, x),
            (y, x+1),
            (y, x-1),
        ]:
            if 0 <= a < h and 0 <= b < w and not visited[a][b] and values[a][b] <= mid:
                visited[a][b] = True
                DFS.append((a, b))
    bad = False
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "P" and not visited[y][x]:
                bad = True
    # Need more power.
    if bad:
        lo = mid + 1
    else:
        hi = mid

print(lo)
