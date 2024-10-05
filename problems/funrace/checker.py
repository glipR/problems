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

EPS = pow(10, -6)

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures funrace solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")
    
    n = int(inp[0])
    nums = list(map(int, inp[1].split()))
    nums.sort()
    
    try:
        proc_best, proc_min, proc_max = list(map(int, process[0].split()))
        if not (proc_min in nums and proc_max in nums):
            return CheckerResult(False, 0, feedback="Min or Max provided not in racers list.")
        lp = -1
        rp = -1
        for x in range(n):
            if nums[x] >= proc_min and lp == -1:
                lp = x
            if nums[x] <= proc_max:
                rp = x
        for x in range(lp, rp):
            if nums[x+1] - nums[x] >= 5:
                return CheckerResult(False, 0, feedback="Any set with this minimum and maximum must have a skill gap of at least 5.")
        length = rp - lp + 1
        judge_best, judge_min, judge_max = list(map(int, judge[0].split()))
        if length > judge_best:
            raise ValueError("======================\n\nWARNING: JUDGE SOLUTION IS INCORRECT. PLEASE CONTACT JACKSON ASAP.\n\n======================")
        if length > proc_best:
            return CheckerResult(False, 0, feedback="Inoptimal")
        if length < proc_best:
            return CheckerResult(False, 0, feedback="There are not that many racers between this min and max.")
        if length == judge_best:
            return CheckerResult(True, kwargs["point_value"])
        else:
            return CheckerResult(False, 0, feedback="Inoptimal")
    except:
        return CheckerResult(False, 0, f"Expected 3 integers, got {process[0]}")

if __name__ == "__main__":
    with open("tests/9.in", "r") as f:
        inp_test = f.read()
    with open("tests/9.out", "r") as f:
        out_test = f.read()
    print(check(out_test.encode("utf-8"), out_test.encode("utf-8"), judge_input=inp_test.encode("utf-8"), point_value=1))
