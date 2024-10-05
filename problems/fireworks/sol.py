n, m, f = list(map(int, input().split()))

grid = [['.' for _ in range(n)] for _ in range(m)]
for _ in range(f):
    x, y = list(map(int, input().split()))
    grid[m-y-1][x] = 'x'

for y in range(m):
    for x in range(n):
        if grid[y][x] != '.': continue
        prev_y = y - 1
        for prev_x in range(x-1, x+2):
            if 0 <= prev_x < n and 0 <= prev_y < m:
                if grid[prev_y][prev_x] != '.':
                    grid[y][x] = '+'

print("\n".join("".join(l) for l in grid))
