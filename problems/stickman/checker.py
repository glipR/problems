from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures stickman solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip()
    process = process_output.decode("utf-8").strip()
    for char in process:
        if char not in "ULDR":
            return CheckerResult(False, 0, "Response contained characters other than ULDR.")
    n, m = map(int, inp[0].split())
    grid = [l.split() for l in inp[1:n+1]]
    coins = inp[n+1:n+1+n]
    start = None
    end = None
    for x in range(n):
        for y in range(m):
            if grid[x][y] in ["S", "G", "W"]:
                if grid[x][y] == "S":
                    start = (x, y)
                if grid[x][y] == "G":
                    end = (x, y)
            else:
                grid[x][y] = int(grid[x][y])
    judge_coins = 0
    judge_sticky = 0
    cur = start
    for direction in judge:
        # if grid[cur[0]][cur[1]] == "W":
        #     raise ValueError("Judge hit a wall!")
        if coins[cur[0]][cur[1]] == "*":
            judge_coins += 1
        if isinstance(grid[cur[0]][cur[1]], int):
            judge_sticky += grid[cur[0]][cur[1]]
        if direction == "U":
            cur = ((cur[0]-1)%n, cur[1])
        elif direction == "D":
            cur = ((cur[0]+1)%n, cur[1])
        elif direction == "L":
            cur = (cur[0], (cur[1]-1)%m)
        elif direction == "R":
            cur = (cur[0], (cur[1]+1)%m)
    if cur != end:
        raise ValueError("Judge didn't return a valid path!")
    process_coins = 0
    process_sticky = 0
    cur = start
    for direction in process:
        if coins[cur[0]][cur[1]] == "*":
            process_coins += 1
        if grid[cur[0]][cur[1]] == "W":
            return CheckerResult(False, 0, "Hit a Wall!")
        if isinstance(grid[cur[0]][cur[1]], int):
            process_sticky += grid[cur[0]][cur[1]]
        if direction == "U":
            cur = ((cur[0]-1)%n, cur[1])
        elif direction == "D":
            cur = ((cur[0]+1)%n, cur[1])
        elif direction == "L":
            cur = (cur[0], (cur[1]-1)%m)
        elif direction == "R":
            cur = (cur[0], (cur[1]+1)%m)
    if cur != end:
        return CheckerResult(0, False, "Path returned doesn't end at the goal.")
    if process_sticky > judge_sticky:
        return CheckerResult(0, False, "Path returned is longer than intended.")
    elif process_sticky < judge_sticky:
        raise ValueError("Judge result not optimal!!!")

    if judge_coins < process_coins:
        return CheckerResult(0, False, "Path returned is longer than intended.")
    elif judge_coins > process_coins:
        raise ValueError("Judge result not optimal!!!")

    return CheckerResult(True, kwargs["point_value"], "Optimal route returned!")
