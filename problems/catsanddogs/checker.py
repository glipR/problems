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
    """Ensures catsanddogs solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")
    n_cats, n_dogs, n_pairings = map(int, inp[0].split())

    pairings = {x+1: {} for x in range(n_cats)}
    for p in range(n_pairings):
        c, d = list(map(int, inp[1+p].split()))
        pairings[c][d] = True
    try:
        process_line_1 = process[0]
        judge_line_1 = judge[0]
        if process_line_1 == "NO":
            if judge_line_1 != "NO":
                return CheckerResult(False, 0, feedback="There is a possible solution.")
            return CheckerResult(True, kwargs["point_value"])
        elif process_line_1 != "YES":
            return CheckerResult(False, 0, feedback=f"First line was not YES or NO: {process_line_1}")
        # YES
        cat_count = {c: 0 for c in range(1, n_cats+1)}
        dog_count = {d: 0 for d in range(1, n_dogs+1)}
        for c in range(n_cats):
            cat, nc, sits, w, dog1, nd1, a, dog2, nd2 = process[1+c].split()
            # Cat #1 sits with Dog #1 and Dog #3
            assert cat == "Cat"
            assert sits == "sits"
            assert w == "with"
            assert dog1 == "Dog"
            assert a == "and"
            assert dog2 == "Dog"
            assert nc.startswith("#")
            assert nd1.startswith("#")
            assert nd2.startswith("#")
            nc = int(nc[1:])
            nd1 = int(nd1[1:])
            nd2 = int(nd2[1:])
            cat_count[nc] += 2
            dog_count[nd1] += 1
            dog_count[nd2] += 1
            
            if nd1 not in pairings[nc] or nd2 not in pairings[nc]:
                return CheckerResult(False, 0, "Seating arrangement given is invalid - non-pairing animals are adjacent.")
            if nd1 == nd2:
                return CheckerResult(False, 0, "2 seater tables do not exist.")
    except Exception as e:
        return CheckerResult(False, 0, feedback=f"Output did not fit usual format: {process[1+c]}")

    for c in cat_count.values():
        if c != 2:
            return CheckerResult(False, 0, feedback=f"Some cat is not seated.")
    for d in dog_count.values():
        if d != 2:
            return CheckerResult(False, 0, feedback=f"Some dog is not adjacent to 2 other cats.")


    if judge_line_1 == "NO":
        raise ValueError("======================\n\nWARNING: JUDGE SOLUTION IS INOPTIMAL. PLEASE CONTACT JACKSON ASAP.\n\n======================")
    else:
        return CheckerResult(True, kwargs["point_value"])

if __name__ == "__main__":
    print(check("""YES
Cat #1 sits with Dog #1 and Dog #3
Cat #2 sits with Dog #2 and Dog #4
Cat #3 sits with Dog #4 and Dog #1
Cat #4 sits with Dog #2 and Dog #3
""".encode("utf-8"), """YES
Cat #1 sits with Dog #1 and Dog #3
Cat #2 sits with Dog #2 and Dog #4
Cat #3 sits with Dog #4 and Dog #1
Cat #4 sits with Dog #2 and Dog #3
""".encode("utf-8"), judge_input="""4 4 12
1 4
1 1
1 3
3 3
3 4
3 1
2 2
2 4
2 1
4 2
4 3
4 1
""".encode("utf-8"), point_value=1))