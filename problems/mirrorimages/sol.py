n = int(input())
graphic = [input() for _ in range(n)]

def flip1(grid):
    return [
        [grid[n-x-1][y] for y in range(n)]
        for x in range(n)
    ]

def flip2(grid):
    return [
        [grid[x][n-y-1] for y in range(n)]
        for x in range(n)
    ]

def flip3(grid):
    return [
        [grid[y][x] for y in range(n)]
        for x in range(n)
    ]

def flip4(grid):
    return [
        [grid[n-y-1][n-x-1] for y in range(n)]
        for x in range(n)
    ]

def to_str(grid):
    return "".join(map("".join, grid))

funcs = [flip1, flip2, flip3, flip4]
graph_set = set(to_str(f1(f2(graphic))) for f1 in funcs for f2 in funcs)
graph_set = graph_set | set(to_str(f1(graphic)) for f1 in funcs)

def nice_print(grid):
    print("\n".join("".join(row) for row in grid))

print(len(graph_set))
