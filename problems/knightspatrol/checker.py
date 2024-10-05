import math, sys
from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures cybercrime solution follows basic problem rules."""
    process = process_output.decode("utf-8").strip().split("\n")
    possible_answers = ["0", "1"]
    for _ in range(6):
        possible_answers = [p + "0" for p in possible_answers] + [p + "1" for p in possible_answers]
    mapping = {}
    try:
        process_lines = [p.split() for p in process]
        for p in process_lines:
            assert len(p) == 2
            assert p[0] in possible_answers
            assert p[1] in possible_answers
            mapping[p[0]] = p[1]
    except:
        return CheckerResult(False, 0, feedback=f"Output did not fit format")

    try:
        assert len(process_lines) == (1 << 7)
        assert len(mapping) == (1 << 7)
    except:
        return CheckerResult(False, 0, feedback=f"Output was not {1 << 7} lines with unique sleeping positions")

    # Rule 1: Everyone shows up in at most 25% of states
    for p in range(7):
        cur = 0
        for r in mapping.values():
            if r[p] == "1":
                cur += 1
        if cur > (1 << 5):
            return CheckerResult(False, 0, feedback=f"One person was on roster for more than 25% of all positions")
    # Rule 2: in at least 12.5% of states, everyone is on patrol
    cur = 0
    for r in mapping.values():
        if r == "1"*7:
            cur += 1
    if cur < (1 << 4):
        return CheckerResult(False, 0, feedback=f"Everyone was on the roster for less than 12.5% of all positions")
    # Rule 3: At least one on patrol
    for r in mapping.values():
        if r == "0"*7:
            return CheckerResult(False, 0, feedback=f"Some positions have no guards on patrol")
    # Rule 4: From any position, we have 7 different adjacent rosters.
    for r in mapping:
        rosters = set()
        for p in range(7):
            new_s = r[:p] + ("1" if r[p] == "0" else "0") + r[p+1:]
            if mapping[new_s] == mapping[r]:
                return CheckerResult(False, 0, feedback=f"From a certain position, flipping a bit still has the same roster.")

    return CheckerResult(True, kwargs["point_value"])
