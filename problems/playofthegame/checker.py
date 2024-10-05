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
    """Ensures playofthegame solution follows basic problem rules and is valid input."""
    inp = kwargs["judge_input"].decode("utf-8").strip().split("\n")
    judge = judge_output.decode("utf-8").strip().split("\n")
    process = process_output.decode("utf-8").strip().split("\n")
    n_players, max_len = map(int, inp[0].split())

    player_strings = []
    for x in range(n_players):
        player_strings.append(inp[x+1])
    begin_state, potg_string = inp[n_players+1].split()

    mapping = {
        "w": 0,
        "a": 1,
        "s": 2,
        "d": 3,
    }
    player_states = []
    for string in player_strings:
        cur_state = [False for key in mapping]
        player_states.append([cur_state[::]])
        for char in string:
            if char == "|":
                player_states[-1].append(cur_state[::])
            else:
                cur_state[mapping[char]] = not cur_state[mapping[char]]
        player_states[-1].append(cur_state[::])

    cur_state = [key in begin_state for key in mapping]
    potg_states = [cur_state[::]]
    for char in potg_string:
        if char == "|":
            potg_states.append(cur_state[::])
        else:
            cur_state[mapping[char]] = not cur_state[mapping[char]]
    potg_states.append(cur_state[::])

    try:
        process_line_1 = process[0]
        if process_line_1 != "No Play of the Game":
            x1, x2, x3, x4, x5, x6, x7, x8, x9 = process_line_1.split(" ")
            assert x1 == "Player"
            assert x2.startswith("#") and 1 <= int(x2[1:]) <= n_players
            assert x3 == "matched"
            assert 0 <= int(x4)
            assert x5 == "frames"
            assert x6 == "starting"
            assert x7 == "at"
            assert x8 == "frame"
            assert x9.startswith("#") and 1 <= int(x9[1:-1])
            process_playernum = int(x2[1:])
            process_nummatched = int(x4)
            process_starting = int(x9[1:-1])
        else:
            process_playernum = None
            process_nummatched = None
            process_starting = None
    except:
        return CheckerResult(False, 0, feedback=f"Output did not fit usual format: {process_line_1}.")

    if judge[0] != "No Play of the Game":
        judge_playernum = int(judge[0].split()[1][1:])
        judge_nummatched = int(judge[0].split()[3])
        judge_starting = int(judge[0].split()[8][1:-1])
    else:
        judge_playernum = None
        judge_nummatched = None
        judge_starting = None

    # Assumes that judge input is good, since we've checked against it's own input.
    if process_playernum is None:
        if judge_playernum is not None:
            return CheckerResult(False, 0, feedback=f"Output claimed no play of the game exists when one does.")
        return CheckerResult(True, kwargs["point_value"])
    else:
        # First, confirm that the information they've given is a valid choice.
        # Check the states line up
        for index in range(process_starting - 1, process_starting + process_nummatched):
            if index - (process_starting - 1) >= len(potg_states):
                return CheckerResult(False, 0, feedback=f"Play of the game provided exceeds the length of the provided peak performance.")
            if index >= len(player_states[process_playernum-1]):
                return CheckerResult(False, 0, feedback=f"Play of the game provided exceeds the length of the provided player input.")
            if potg_states[index - (process_starting - 1)] != player_states[process_playernum-1][index]:
                return CheckerResult(False, 0, feedback=f"Play of the game provided does not match peak performance output for suggested frames.")
        # We are valid. But are we long enough.
        if process_nummatched > judge_nummatched:
            raise ValueError("======================\n\nWARNING: JUDGE SOLUTION IS INOPTIMAL. PLEASE CONTACT JACKSON ASAP.\n\n======================")
        elif process_nummatched < judge_nummatched:
            return CheckerResult(False, 0, feedback=f"Play of the game given is shorter than that provided by the judge.")
        else:
            return CheckerResult(True, kwargs["point_value"])

if __name__ == "__main__":
    print(check("""Player #1 matched 3 frames starting at frame #2.
""".encode("utf-8"), """Player #1 matched 3 frames starting at frame #2.
""".encode("utf-8"), judge_input="""2 15
as|s|sda|ds|sw
s|das|ds|s|as
as s|das|ds|s
""".encode("utf-8"), point_value=1))