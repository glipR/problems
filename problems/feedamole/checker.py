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

EPS = pow(10, -6)

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures funrace solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")

    w, h, t = list(map(int, inp[0].split()))

    lines = [inp[i].split() for i in range(1, t+1)]

    states = [[[False for _ in range(h)] for _ in range(w)] for _ in range(t)]

    for i in range(t):
        m = int(lines[i][0])
        for p in range(m):
            x, y = int(lines[i][2*p+1])-1, int(lines[i][2*p+2])-1
            states[i][x][y] = True

    try:
        proc_best = int(process[0])
    except:
        return CheckerResult(False, 0, feedback="First line of output was not a single integer.")
    judge_best = int(judge[0])

    # Validate choices.
    try:
        proc_choices = [
            list(map(int, process[i].split()))
            for i in range(1, t+1)
        ]
        assert set(map(len, proc_choices)) == { 2 }
    except:
        return CheckerResult(False, 0, feedback="T lines of feedback did not contain two space-separated integers")

    for x, y in proc_choices:
        if not 1 <= x <= w and 1 <= y <= h:
            return CheckerResult(False, 0, feedback="T lines of feedback contained integers outside of expected range")
    for (a, b), (x, y) in zip(proc_choices[:-1], proc_choices[1:]):
        total_diff = abs(a-x) + abs(b-y)
        if total_diff > 1:
            return CheckerResult(False, 0, feedback="Movements given are not within 1-distance of eachother.")

    # This must be valid. validate the score.
    score = sum(states[i][x-1][y-1] for i, (x, y) in enumerate(proc_choices))

    if score != proc_best:
        return CheckerResult(False, 0, feedback="Integer printed is not the score of your printed path.")
    if score > judge_best:
        raise ValueError("======================\n\nWARNING: JUDGE SOLUTION IS INCORRECT. PLEASE CONTACT JACKSON ASAP.\n\n======================")
    if judge_best > score:
        return CheckerResult(False, 0, feedback="Inoptimal")
    if score == judge_best:
        return CheckerResult(True, kwargs["point_value"])

if __name__ == "__main__":
    with open("tests/1_1.in", "r") as f:
        inp_test = f.read()
    with open("tests/1_1.out", "r") as f:
        out_test = f.read()
    print(check(out_test.encode("utf-8"), out_test.encode("utf-8"), judge_input=inp_test.encode("utf-8"), point_value=1))
