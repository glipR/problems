import sys
from random import randint

DEBUG = True

def test_res(n, write_fn, read_fn, points):
    write_fn(str(n))

    fake_coins = set()
    while len(fake_coins) < 2:
        fake_coins.add(randint(1, n))

    if DEBUG:
        print("FAKE COINS: ", " ".join(map(str, fake_coins)), file=sys.stderr)

    GUESSES_LEFT = 22

    while GUESSES_LEFT > -22:
        try:
            guess = read_fn().split()
            if DEBUG:
                print(" ".join(guess), file=sys.stderr)
            if guess[0] == "TEST":
                assert guess.count("|") == 1
                idx = guess.index("|")
                left = list(map(int, guess[1:idx]))
                right = list(map(int, guess[idx+1:]))
            elif guess[0] == "ANS":
                guess_coin = list(map(int, guess[1:]))
                if set(guess_coin) == set(fake_coins):
                    if GUESSES_LEFT >= 0:
                        return CheckerResult(True, points, f"Correct after {22 - GUESSES_LEFT} queries!")
                    return CheckerResult(False, 0, f"Too many queries ({22 - GUESSES_LEFT})")
                else:
                    return CheckerResult(False, 0, "Incorrect guess")
            else:
                raise ValueError()
        except:
            return CheckerResult(False, 0, "Invalid Output")
        if len(set(left)) != len(left):
            return CheckerResult(False, 0, "Left coins have duplicates")
        if len(set(right)) != len(right):
            return CheckerResult(False, 0, "Right coins have duplicates")
        if len(set(left + right)) != len(left) + len(right):
            return CheckerResult(False, 0, "Left and Right sides have the shared values")
        if len(left) > len(right):
            write_fn("LEFT")
            if DEBUG:
                print("LEFT", file=sys.stderr)
        elif len(left) < len(right):
            write_fn("RIGHT")
            if DEBUG:
                print("RIGHT", file=sys.stderr)
        else:
            left_amount = 0
            right_amount = 0
            for coin in fake_coins:
                if coin in left:
                    left_amount += 1
                if coin in right:
                    right_amount += 1
            if left_amount > right_amount:
                write_fn("LEFT")
                if DEBUG:
                    print("LEFT", file=sys.stderr)
            elif left_amount < right_amount:
                write_fn("RIGHT")
                if DEBUG:
                    print("RIGHT", file=sys.stderr)
            else:
                write_fn("EQUAL")
                if DEBUG:
                    print("EQUAL", file=sys.stderr)
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
