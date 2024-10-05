w, h, t = list(map(int, input().split()))

lines = [input().split() for _ in range(t)]

states = [[[False for _ in range(h)] for _ in range(w)] for _ in range(t)]

for i in range(t):
    m = int(lines[i][0])
    for p in range(m):
        x, y = int(lines[i][2*p+1])-1, int(lines[i][2*p+2])-1
        states[i][x][y] = True

def brute_search(cur_time, cur_x, cur_y):
    if cur_time == t:
        return 0, []
    cur_val = states[cur_time][cur_x][cur_y]
    # 5 options: UDLR/stay still
    opts = []
    for xd, yd in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (0, 0),
    ]:
        new_x, new_y = cur_x + xd, cur_y + yd
        if not (0 <= new_x < w and 0 <= new_y < h):
            continue
        opts.append(brute_search(cur_time+1, new_x, new_y))
    best_score, best_moves = max(opts)
    return best_score + cur_val, best_moves + [(cur_x, cur_y)]

opts = []
for x in range(w):
    for y in range(h):
        opts.append(brute_search(0, x, y))

score, moves = max(opts)

print(score)
for x, y in moves[::-1]:
    print(x+1, y+1)
