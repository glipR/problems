import math

TESTING = False

if TESTING:
    class CheckerResult:
        def __init__(self, *args, **kwargs) -> None:
            self.args = args
            self.kwargs = kwargs
        
        def __repr__(self) -> str:
            return f"Result. args:{self.args}, kwargs:{self.kwargs}"
else:
    from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures inflatedstonks solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")
    n = int(inp[0])
    grid = inp[1:n+1]
    values = [
        list(map(int, x.split()))
        for x in inp[n+1:2*n+1]
    ]
    translation = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    # Validate player input
    if len(process) == 0:
        return CheckerResult(False, 0, feedback=f"Empty output.")
    try:
        proc_days = int(process[0])
    except:
        return CheckerResult(False, 0, feedback=f"Expected number of mining trips, got {process[0]}")

    if len(process) < proc_days + 1:
        return CheckerResult(False, 0, feedback=f"Said you have {proc_days} mining trips, but only have {len(process)} lines of output.")
    proc_trips = []
    try:
        for i in range(proc_days):
            y, x = list(map(int, process[i+1].split()))
            proc_trips.append((y, x))
    except:
        return CheckerResult(False, 0, feedback=f"Solution did not state mining locations in valid format.")

    # Check overall cost of trip.
    mined = [[False for _ in range(n)] for _ in range(n)]
    proc_total = 0
    for y, x in proc_trips:
        new_locations = 0
        new_diamonds = 0
        while 0 <= y < n and 0 <= x < n:
            if mined[y][x]:
                break
            mined[y][x] = True
            new_locations += 1
            new_diamonds += values[y][x]
            direction = grid[y][x]
            y, x = y + translation[direction][0], x + translation[direction][1]
        proc_total += new_locations * new_diamonds
    
    judge_days = int(judge[0])
    judge_trips = []
    for i in range(judge_days):
        y, x = list(map(int, judge[i+1].split()))
        judge_trips.append((y, x))

    # Check overall cost of judge trip.
    mined = [[False for _ in range(n)] for _ in range(n)]
    judge_total = 0
    for y, x in judge_trips:
        new_locations = 0
        new_diamonds = 0
        while 0 <= y < n and 0 <= x < n:
            if mined[y][x]:
                break
            mined[y][x] = True
            new_locations += 1
            new_diamonds += values[y][x]
            direction = grid[y][x]
            y, x = y + translation[direction][0], x + translation[direction][1]
        judge_total += new_locations * new_diamonds
    
    if judge_total < proc_total:
        raise ValueError("======================\n\nWARNING: JUDGE SOLUTION IS INOPTIMAL. PLEASE CONTACT JACKSON ASAP.\n\n======================")
    elif judge_total > proc_total:
        return CheckerResult(False, 0, feedback=f"Mining trips selected are inoptimal. Judge moves price by {judge_total} and Process moves price by {proc_total}.")
    return CheckerResult(True, kwargs["point_value"])

if __name__ == "__main__":
    print(check("""7
3 0
3 3
0 3
0 0
2 3
2 0
1 3
""".encode("utf-8"), """7
0 3
0 0
2 3
2 0
1 3
3 0
3 3
""".encode("utf-8"), judge_input="""4
RRDL
LUDR
UULL
RRLL
4 8 2 10
1 1 1 1
1 1 1 1
6 1 1 4
""".encode("utf-8"), point_value=1))