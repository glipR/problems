from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    lines = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge_lines = judge_output.decode("utf-8").strip().split("\n")
    try:
        process_lines = process_output.decode("utf-8").strip().split("\n")  
        assert len(process_lines) == len(judge_lines)
    except:
        return CheckerResult(False, 0, "Did not respond with T integers.")
    tests = int(lines[0])
    for case in range(tests):

        judge_int = int(judge_lines[case])
        try:
            process_int = int(process_lines[case])
        except:
            return CheckerResult(False, 0, feedback="Output was not an integer.")
        
        a, b = list(map(int, lines[case+1].split()))

        if process_int == -1:
            if process_int == judge_int:
                continue
            return CheckerResult(False, 0, f"{a} {b} does have a triple (with {judge_int}), yet you responded -1.")
        
        if process_int != 0 and (
            (process_int * process_int == a * a + b * b) or
            (a * a == process_int * process_int + b * b) or
            (b * b == process_int * process_int + a * a)
        ):
            if judge_int == -1:
                raise ValueError(f"Judge response {a} {b} was incorrect! Please contact contest organiser. You've found a bug.")
            continue
        return CheckerResult(False, 0, f"Wrong. {a} {b} {process_int} does not form a triangle.")

    return CheckerResult(True, kwargs["point_value"], "Correct Answer")
