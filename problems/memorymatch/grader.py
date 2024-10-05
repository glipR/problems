import sys
import random
from dmoj.graders import InteractiveGrader
from dmoj.result import CheckerResult

class Grader(InteractiveGrader):
    def interact(self, case, interactor):
        tests = 10**2
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        card_options = [
            a + b
            for a in alph for b in alph
        ]

        interactor.writeln(f"{tests}")

        for cur_case in range(tests):
            random.shuffle(card_options)
            N = random.randint(40, 80)
            cards = card_options[:N] + card_options[:N]
            random.shuffle(cards)
            queries = 2 * N
            matched = [False] * (2 * N)
            interactor.writeln(f"{N}")
            while True:
                if queries <= 0:
                    return CheckerResult(False, 0, "Ran out of Queries")
                line = interactor.readln().decode('utf-8').strip().split()
                if len(line) != 2:
                    return CheckerResult(False, 0, "Invalid Query: {}".format(" ".join(line)))
                try:
                    line[0] = int(line[0])
                    line[1] = int(line[1])
                except:
                    return CheckerResult(False, 0, f"Query parameters where not integers (Got {line[0]} and {line[1]}).")
                if not (1 <= line[0] <= 2*N and 1 <= line[1] <= 2*N):
                    return CheckerResult(False, 0, f"Query parameters did not sit between 1 and 2N (Got {line[0]} and {line[1]}).")
                # Check, what are they?
                a = cards[line[0]-1]
                b = cards[line[1]-1]
                if a == b:
                    matched[line[0]-1] = True
                    matched[line[1]-1] = True
                solved = int(sum(matched) == 2 * N)
                interactor.writeln(f"{a} {b} {solved}")
                if solved:
                    break
        return CheckerResult(True, case.points, "Passed all tests!")
