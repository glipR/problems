from dmoj.result import CheckerResult

def check(process_output:bytes, judge_output:bytes, **kwargs):
    """Ensures scuttlebug jamboree is a correct path, and minimal."""
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = judge_output.decode("utf-8").strip().split("\n")
    judge_ints = list(map(int, judge[0].split()))
    try:
        process_ints = list(map(int, process[0].split()))
        assert len(process_ints) == 2
    except:
        return CheckerResult(False, 0, feedback="Output did not being with 2 integers.")
    
    if process_ints[1] > 502:
        return CheckerResult(False, 0, feedback="Gave length longer than 500, which should be impossible.")
    
    path = [loc for loc in process[1:]]
    if len(path) != process_ints[1]:
        return CheckerResult(False, 0, feedback="Path length did not match l given.")

    # Now, check validity of the path.
    # Step 1: Each non-river location appears at most once.
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    counts = {k: 0 for k in inp[1:]}
    for loc in path:
        if loc in ["N", "S"]:
            continue
        if loc not in counts:
            return CheckerResult(False, 0, feedback="Gave lilypad coord that does not exist.")
        counts[loc] += 1
        if counts[loc] >= 2:
            return CheckerResult(False, 0, feedback="Lilypad met twice.")

    h, n, b = list(map(int, inp[0].split()))

    n_path = [loc for loc in path if loc in "NS"]
    if len(n_path) != 2 * b + 1:
        return CheckerResult(False, 0, feedback="Did not visit the north side b times or south side b+1 times.")
    for x in range((len(n_path) + 1) // 2):
        if n_path[2*x] != "S":
            return CheckerResult(False, 0, "Failed SNSNS check")
    for x in range(len(n_path) // 2):
        if n_path[2*x+1] != "N":
            return CheckerResult(False, 0, "Failed SNSNS check")

    # Now just have to check that every edge is within distance.
    for loc1, loc2 in zip(path[:-1], path[1:]):
        if loc1 == "N":
            if loc2 == "S":
                if h * h > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")
            else:
                d = (h - int(loc2.split(" ")[1])) * (h - int(loc2.split(" ")[1]))
                if d > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")
        elif loc1 == "S":
            if loc2 == "N":
                if h * h > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")
            else:
                if int(loc2.split(" ")[1]) * int(loc2.split(" ")[1]) > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")
        else:
            if loc2 == "N":
                d = (h - int(loc1.split(" ")[1])) * (h - int(loc1.split(" ")[1]))
                if d > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")
            elif loc2 == "S":
                if int(loc1.split(" ")[1]) * int(loc1.split(" ")[1]) > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")
            else:
                d = (
                    (int(loc1.split(" ")[0]) - int(loc2.split(" ")[0])) * (int(loc1.split(" ")[0]) - int(loc2.split(" ")[0])) +
                    (int(loc1.split(" ")[1]) - int(loc2.split(" ")[1])) * (int(loc1.split(" ")[1]) - int(loc2.split(" ")[1]))
                )
                if d > process_ints[0]:
                    return CheckerResult(False, 0, f"Invalid path {h} {loc1} {loc2} {process_ints}")

    if judge_ints[0] < process_ints[0]:
        return CheckerResult(False, 0, feedback="Choice of d is inoptimal")
    elif judge_ints[0] == process_ints[0]:
        return CheckerResult(True, kwargs["point_value"])
    else:
        raise ValueError("Submission d is smaller than judge d!")
