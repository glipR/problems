w, h, t = list(map(int, input().split()))

lines = [input().split() for _ in range(t)]

states = [[[False for _ in range(h)] for _ in range(w)] for _ in range(t)]

for i in range(t):
    m = int(lines[i][0])
    for p in range(m):
        x, y = int(lines[i][2*p+1])-1, int(lines[i][2*p+2])-1
        states[i][x][y] = True

# DP[i][x][y] := score

DP = [
    [
        [int(states[i][x][y]) for y in range(h)]
        for x in range(w)
    ]
    for i in range(t)
]

moves = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (0, 0),
]

for i in range(t-2, -1, -1):
    for x in range(w):
        for y in range(h):
            best = 0
            for dx, dy in moves:
                newx, newy = x+dx, y+dy
                if 0 <= newx < w and 0 <= newy < h:
                    best = max(best, DP[i+1][newx][newy])
            DP[i][x][y] = best + states[i][x][y]

best, cx, cy = max((DP[0][x][y], x, y) for x in range(w) for y in range(h))

points = [(cx, cy)]

for i in range(1, t):
    _, cx, cy = max([
        (DP[i][cx+dx][cy+dy], cx+dx, cy+dy)
        for dx, dy in moves
        if 0 <= cx+dx < w and 0 <= cy+dy < h
    ])
    points.append((cx, cy))

print(best)
for x, y in points:
    print(x+1, y+1)

