import math

from dmoj.result import CheckerResult

def check(process_output: bytes, judge_output: bytes, **kwargs):
    inp = int(kwargs["judge_input"].decode("utf-8").strip())
    judge = judge_output.decode("utf-8").strip()
    process = process_output.decode("utf-8").strip()

    judge = float(judge)

    try:
        process = float(process)
    except:
        return CheckerResult(False, 0, f"Output is not a number, got {process}")

    large_error = math.log(inp)
    small_error = 1/inp + 2*math.sqrt(inp)*math.log(1 + math.log(inp) / inp) + math.sqrt(inp) / (1<<40)

    score = 0
    if abs(judge - process) < 2*large_error:
        score = 0.3 * kwargs["point_value"]
    if abs(judge - process) < 2*small_error:
        score = kwargs["point_value"]

    return CheckerResult(score != 0, score, "")

