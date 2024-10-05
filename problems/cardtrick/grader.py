import sys
import random
from dmoj.graders import StandardGrader
from dmoj.result import Result

class Grader(StandardGrader):
    def grade(self, case):
        res = Result(case)

        tests = 10**5
        suit = "SDHC"
        vals = "A23456789TJQK"
        deck = [s+v for s in suit for v in vals]

        given = [None]*tests
        for c in range(tests):
            random.shuffle(deck)
            given[c] = " ".join(deck[:5])

        gerald_stuff = [None] * tests

        leanne_input = f"0\n{tests}\n" + "\n".join(given)

        self._launch_process(case)

        error = self._interact_with_process(case, res, leanne_input.encode("utf-8"))

        process = self._current_proc

        self.populate_result(error, res, process)

        output = res.proc_output

        if error:
            res.result_flag = Result.RTE
            res.extended_feedback = "Leanne encountered a run time error."
            return res

        try:
            o = output.decode().strip().split("\n")
            assert len(o) == tests
            for i, line in enumerate(o):
                cards = line.strip().split(" ")
                assert len(cards) == 4
                assert len(set(cards)) == 4
                for c in cards:
                    assert len(c) == 2 and c[0] in suit and c[1] in vals
                    assert c in given[i]
                gerald_stuff[i] = line
        except:
            res.result_flag = Result.WA
            res.extended_feedback = f"Leanne gave output that was not {tests} lines with 4 cards {str(output)[:40]}."
        else:

            gerald_input = f"1\n{tests}\n" + "\n".join(gerald_stuff)

            self._launch_process(case)

            error = self._interact_with_process(case, res, gerald_input.encode("utf-8"))

            process = self._current_proc

            self.populate_result(error, res, process)
            output2 = res.proc_output

            if error:
                res.result_flag = Result.RTE
                res.extended_feedback = "Gerald encountered a run time error."
                return res

            try:
                o2 = output2.decode().strip().split("\n")

                good = True
                assert len(o2) == tests
                for i, c in enumerate(o2):
                    c = c.strip()
                    assert len(c) == 2 and c[0] in suit and c[1] in vals
                    assert c not in gerald_stuff[i]
                    if c not in given[i]:
                        good = False
            
                if good:
                    res.result_flag = Result.AC
                    res.extended_feedback = "Correct!"
                    res.points = case.points
                else:
                    res.result_flag = Result.WA
                    res.extended_feedback = "Gerald answered incorrectly."
            except:
                res.result_flag = Result.WA
                res.extended_feedback = f"Gerald gave output that was not {tests} lines of cards that Leanne did not show."

        return res
