from random import randint
import sys

DEBUG = True

def test_res(n, write_fn, read_fn, points):
    write_fn(str(n))

    fake_coins = set()
    while len(fake_coins) < 3:
        fake_coins.add(randint(1, n))

    if DEBUG:
        print("FAKE COINS: ", " ".join(map(str, fake_coins)), file=sys.stderr)

    GUESSES_LEFT = 27

    while GUESSES_LEFT > -27:
        try:
            guess = read_fn().split()
            if DEBUG:
                print(" ".join(guess), file=sys.stderr)
            if guess[0] == "TEST":
                assert guess.count("|") == 2
                idx1 = guess.index("|")
                idx2 = idx1 + guess[idx1+1:].index("|") + 1
                left = guess[1:idx1]
                if len(left) == 1 and left[0] == "":
                    left = []
                left = list(map(int, left))
                middle = guess[idx1+1:idx2]
                if len(middle) == 1 and middle[0] == "":
                    middle = []
                middle = list(map(int, middle))
                right = guess[idx2+1:]
                if len(right) == 1 and right[0] == "":
                    right = []
                right = list(map(int, right))
            elif guess[0] == "ANS":
                guess_coin = list(map(int, guess[1:]))

                if set(guess_coin) == set(fake_coins):
                    if GUESSES_LEFT >= 0:
                        return CheckerResult(True, points, f"Correct after {27 - GUESSES_LEFT} queries!")
                    return CheckerResult(False, 0, f"Too many queries ({27 - GUESSES_LEFT})")
                else:
                    return CheckerResult(False, 0, f"Incorrect guess {fake_coins} vs. {guess_coin}")
            else:
                raise ValueError()
        except:
            return CheckerResult(False, 0, "Invalid Output")
        if len(set(left)) != len(left):
            return CheckerResult(False, 0, "Left coins have duplicates")
        if len(set(middle)) != len(middle):
            return CheckerResult(False, 0, "Middle coins have duplicates")
        if len(set(right)) != len(right):
            return CheckerResult(False, 0, "Right coins have duplicates")
        if len(set(left + right + middle)) != len(left) + len(right) + len(middle):
            return CheckerResult(False, 0, "Left and Right sides have the shared values")

        score_l = len(left) + sum(0.1 for fake in fake_coins if fake in left)
        score_m = len(middle) + sum(0.1 for fake in fake_coins if fake in middle)
        score_r = len(right) + sum(0.1 for fake in fake_coins if fake in right)

        score_map = {}
        score_map[score_l] = score_map.get(score_l, []) + [1]
        score_map[score_m] = score_map.get(score_m, []) + [2]
        score_map[score_r] = score_map.get(score_r, []) + [3]

        response = []
        for key in sorted(score_map.keys(), reverse=True):
            response.append(" ".join(map(str, score_map[key])))
        write_fn(" > ".join(response))
        if DEBUG:
            print(" > ".join(response), file=sys.stderr)

        GUESSES_LEFT -= 1



    return CheckerResult(False, 0, "Too many queries")

if not(len(sys.argv) > 1 and sys.argv[1] == "local"):
    from dmoj.graders import InteractiveGrader
    from dmoj.result import CheckerResult

    class Grader(InteractiveGrader):
        def interact(self, case, interactor):
            n = int(case.input_data().decode().strip())
            write_fn = interactor.writeln
            read_fn = lambda: interactor.readln().decode()
            return test_res(n, write_fn, read_fn, case.points)
else:
    CheckerResult = lambda a, b, c: (a, b, c)
    res = test_res(int(sys.argv[2]), print, input, 1)

