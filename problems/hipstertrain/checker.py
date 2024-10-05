from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    judge_in = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge_out = list(map(int, judge_output.decode("utf-8").strip().split("\n")[0].split(" ")))
    try:
        process_out = list(map(int, process_output.decode("utf-8").strip().split("\n")[0].split(" ")))
        assert len(process_out) == len(judge_out)
    except:
        return CheckerResult(False, 0, "Did not respond with S integers.")

    if sum(process_out) < sum(judge_out):
        return CheckerResult(False, 0, "Responded with less hipsters than the judge.")
    # Verify that the hipster choice is correct. Simulate.
    s, cap = map(int, judge_in[0].split(" "))
    cur = 0
    values = [list(map(int, judge_in[i].split(" "))) for i in range(1, len(judge_in))]
    c, h, x, y, z = range(5)
    total = 0
    for i, v in enumerate(values):
        if process_out[i] < 0:
            return CheckerResult(False, 0, "Output invalid.", extended_feedback="Hipsters were negative.")
        if process_out[i] > v[h]:
            return CheckerResult(False, 0, "Output invalid.", extended_feedback="Boarded more hipsters than available.")
        cap += v[c]
        cur = max(0, cur - v[x])
        if process_out[i] > 0:
            cur += process_out[i] * (1 + v[z])
            if (cur - 1 - v[z]) * 100 > v[y] * cap:
                return CheckerResult(False, 0, "Output invalid.", extended_feedback="Hipsters boarded even when more than y cap.")
            if cur > cap:
                return CheckerResult(False, 0, "Output invalid.", extended_feedback="Hipsters boarding past capacity.")

    if sum(process_out) > sum(judge_out):
        raise ValueError("Woops! You responded with something better than the judge. Please contact the contest organiser immediately.")
    return CheckerResult(True, kwargs["point_value"], "Valid response.")
