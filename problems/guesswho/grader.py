import sys
from dmoj.result import CheckerResult
from dmoj.graders.interactive import InteractiveGrader

DEBUG = False

class Grader(InteractiveGrader):

    def writeln(self, interactor, text):
        interactor.writeln(text)
        if DEBUG:
            print(text, file=sys.stderr)

    def readln(self, interactor):
        res = interactor.readln()
        if DEBUG:
            print(f"Response: {res}", file=sys.stderr)
        return res

    def interact(self, case, interactor):
        in_data = case.input_data().decode('utf-8').split("\n")

        queries = 0
        n, f = map(int, in_data[0].split())
        self.writeln(interactor, f"{n} {f}")
        

        features = []
        indexes = {}
        for i in range(f):
            features.append(in_data[i + 1])
            indexes[features[-1]] = i
            self.writeln(interactor, in_data[i + 1])
        characters = []
        for i in range(n):
            characters.append(in_data[i + 1 + f].split())
            self.writeln(interactor, in_data[i + 1 + f])
        correct_index = int(in_data[n + 1 + f])
        if DEBUG:
            print(f"Correct index: {correct_index}", file=sys.stderr)
            print(" ".join(characters[correct_index]), file=sys.stderr)
        
        try:
            while True:
                queries += 1

                line = self.readln(interactor).decode('utf-8').strip().split()
                if line[0] == "QUERY":
                    f, e, v = line[1:]
                    if f not in indexes:
                        interactor.close()
                        return CheckerResult(False, 0, f"Unknown feature {f}")
                    if e != "=":
                        interactor.close()
                        return CheckerResult(False, 0, f"Expected '=' got {e}")
                    if (characters[correct_index][indexes[f]] == v):
                        self.writeln(interactor, "YES")
                    else:
                        self.writeln(interactor, "NO")
                elif line[0] == "GUESS":
                    r = int(line[1])
                    if not (0 < r <= n):
                        interactor.close()
                        return CheckerResult(False, 0, f"Invalid guess: {r}")
                    if correct_index == r - 1:
                        interactor.close()
                        return CheckerResult(True, case.points, f"Got the answer in {queries} queries")
                    else:
                        interactor.close()
                        return CheckerResult(False, 0, f"Guess incorrectly in {queries} queries")
                else:
                    raise ValueError(f"Unknown command {line[0]}")
                if queries >= 20:
                    interactor.close()
                    return CheckerResult(False, 0, f"Too many queries")
        except Exception as e:
            interactor.close()
            return CheckerResult(False, 0, f"Malformed input when interacting.")



