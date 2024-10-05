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

DAY, DURATION, STRENGTH, CAFFEINE, INDEX = range(5)

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures coffeecrisis solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")
    days, specials = map(int, inp[0].split())
    
    coffees = [
        list(map(int, inp[1+i].split()))
        for i in range(specials)
    ]

    judge_assignments = int(judge[0])

    try:
        process_assignments = int(process[0])
        process_punchcard = process[1]
        if len(process_punchcard) != specials:
            return CheckerResult(False, 0, feedback=f"Punchcard length is incorrect.")
        for char in process_punchcard:
            if char not in "-*":
                return CheckerResult(False, 0, feedback="Punchcard contains illegal characters.")
    except:
        return CheckerResult(False, 0, feedback=f"Output did not fit usual format: {process[0]}\n{process[1]}.")

    # Check that process solution makes sense.
    used_coffees = [x for x in range(specials) if process_punchcard[x] == "*"]
    used_coffees = list(sorted(used_coffees, key=lambda x: coffees[x][DAY]))
    if len(used_coffees) != 0:
        actual_assignments = coffees[used_coffees[0]][DAY] - 1
        for k in range(len(used_coffees)):
            i = used_coffees[k]
            assignments = coffees[i][STRENGTH] * min(days - coffees[i][DAY] + 1, coffees[i][DURATION])
            delay = max(coffees[i][DURATION], coffees[i][CAFFEINE])
            extra = max(0, 
                days - coffees[i][DAY] - delay + 1
                if k == len(used_coffees) - 1 else
                coffees[used_coffees[k+1]][DAY] - coffees[i][DAY] - delay
            )
            if k != len(used_coffees) - 1:
                if coffees[used_coffees[k+1]][DAY] - coffees[i][DAY] - delay < 0:
                    return CheckerResult(False, 0, feedback="Two coffees given to be drunk are too close to each other, either due to duration or caffiene content.")
            actual_assignments += (assignments + extra)
    else:
        actual_assignments = days
    
    if actual_assignments != process_assignments:
        return CheckerResult(False, 0, feedback="Calculated assignments completed does not match the special coffees you've chosen.")

    if actual_assignments < judge_assignments:
        return CheckerResult(False, 0, feedback=f"Solution given does not solve the optimal number of assignments.")
    elif actual_assignments > judge_assignments:
        raise ValueError("======================\n\nWARNING: JUDGE SOLUTION IS INOPTIMAL. PLEASE CONTACT JACKSON ASAP.\n\n======================")
    else:
        return CheckerResult(True, kwargs["point_value"])

if __name__ == "__main__":
    print(check("""362
--**
""".encode("utf-8"), """362
--**
""".encode("utf-8"), judge_input="""30 4
6 12 20 14
19 12 10 100
13 8 20 30
3 10 20 4
""".encode("utf-8"), point_value=1))
