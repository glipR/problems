# grid size is very small here - just hardcode some tests.

import sys

n, m = list(map(int, input().split()))

lines = [list(input()) for _ in range(n)]

n_objectives = 2

for x in range(n):
    for y in range(m):
        if lines[x][y] == "S":
            spawn = (x, y)
        elif lines[x][y] == "A":
            lines[x][y] = 1
        elif lines[x][y] == "B":
            lines[x][y] = 1<<1
        elif lines[x][y] == "G":
            goal = (x, y)

def node_encode(x, y, cur_state):
    return m*x + y + cur_state * n * m

def node_decode(pos):
    cur_state = pos // (n * m)
    if cur_state == 1<<n_objectives:
        return "constant"
    pos %= n * m
    x = pos // m
    pos %= m
    y = pos
    return x, y, cur_state

matrix = [
    [
        0 for _ in range(n*m*(1<<n_objectives) + 1)
    ] for _ in range(n*m*(1<<n_objectives))
]

for x in range(n):
    for y in range(m):
        if lines[x][y] == "X":
            continue
        for cur_state in range(1<<n_objectives):
            # From this, we can move U/D/L/R
            this_node = node_encode(x, y, cur_state)
            if (x, y) == goal and cur_state == (1<<n_objectives)-1:
                # We are done!
                matrix[this_node][this_node] = 1
                continue
            options = []
            for a, b in [
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1),
            ]:
                new_state = cur_state
                if not (0 <= a < n and 0 <= b < m):
                    a, b = x, y
                if lines[a][b] == "X":
                    a, b = x, y
                if type(lines[a][b]) == int:
                    new_state |= lines[a][b]
                options.append(node_encode(a, b, new_state))
            # negate so the postive values are equal to this.
            matrix[this_node][this_node] = -1
            # 1 more step
            matrix[this_node][-1] = 1
            for option in options:
                matrix[this_node][option] += 1/4

def reduced_row_echelon_form(matrix):
    rowCount = len(matrix)
    colCount = len(matrix[0])
    lead = 0
    for r in range(rowCount):
        if colCount <= lead: return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if rowCount == i:
                i = r
                lead = lead + 1
                if colCount == lead:
                    return
        # swap rows i and r
        matrix[i], matrix[r] = matrix[r], matrix[i]
        if matrix[r][lead] != 0:
            div = matrix[r][lead]
            for c in range(colCount):
                matrix[r][c] /= div
        for i in range(rowCount):
            if i != r:
                deduction = matrix[i][lead]
                for c in range(colCount):
                    matrix[i][c] -= deduction * matrix[r][c]
        lead += 1

reduced_row_echelon_form(matrix)

start_node = node_encode(*spawn, 0)
# Find the row with col value at start position equal to 1.
for r in range(len(matrix)):
    if matrix[r][start_node] != 0:
        print("non-zero row", file=sys.stderr)
        for idx, val in enumerate(matrix[r]):
            if val != 0:
                print(node_decode(idx), val, file=sys.stderr)

        print(-matrix[r][-1])

