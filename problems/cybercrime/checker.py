import math
from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures cybercrime solution follows basic problem rules."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")
    judge_ints = list(map(int, judge[0].split()))
    try:
        process_ints = list(map(int, process[0].split()))
        assert 1 <= len(process_ints) <= 3
        assert len(list(set(process_ints))) == len(process_ints)
    except:
        return CheckerResult(False, 0, feedback=f"Output did not being with 1-3 distinct integers: {process}.")

    n, m = list(map(int, inp[0].split(" ")))
    dna = inp[1].split(" ")
    mutated = inp[2].split(" ")
    probs = list(map(float, inp[3].split(" ")))

    # Check that every answer they've given is a valid choice
    try:
        for p in process_ints:
            # We are starting from position p-1
            for x in range(m):
                pos_dna = (p-1+x) % n
                if probs[x] == 0:
                    assert dna[pos_dna] == mutated[x]
                elif probs[x] == 1:
                    assert dna[pos_dna] != mutated[x]
    except AssertionError:
        return CheckerResult(False, 0, feedback="WA")

    if len(process_ints) > len(judge_ints):
        raise ValueError("Oops! Our solution code isn't quite right. Please contact one of the contest organizers immediately (Error code 1).")

    elif len(process_ints) < len(judge_ints):
        return CheckerResult(False, 0, feedback="WA")

    # Start checking relative errors.
    judge_probs = [0] * len(judge_ints)
    process_probs = [0] * len(process_ints)

    for x in range(len(judge_ints)):
        for y in range(m):
            pos_dna = (judge_ints[x]-1+y) % n
            if probs[y] not in [0, 1]:
                if dna[pos_dna] != mutated[y]:
                    judge_probs[x] += math.log(probs[y])
                else:
                    judge_probs[x] += math.log(1 - probs[y])
    for x in range(len(process_ints)):
        for y in range(m):
            pos_dna = (process_ints[x]-1+y) % n
            if probs[y] not in [0, 1]:
                if dna[pos_dna] != mutated[y]:
                    process_probs[x] += math.log(probs[y])
                else:
                    process_probs[x] += math.log(1 - probs[y])

    import sys

    judge_probs.sort()
    process_probs.sort() 

    for x in range(len(judge_probs)):
        diff = judge_probs[x] - process_probs[x]
        # Expected: If anything, positive.
        if diff < -0.001:
            raise ValueError("Oops! Our solution code isn't quite right. Please contact one of the contest organizers immediately (Error code 2).")
        elif diff > 0.001:
            return CheckerResult(False, 0, "WA")

    # All are within 0.01 of expected answers, and valid choices. AC!
    return CheckerResult(True, kwargs["point_value"])
