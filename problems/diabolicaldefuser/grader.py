import sys
import time
import random
from dmoj.graders import StandardGrader
from dmoj.result import Result

class Grader(StandardGrader):
    def grade(self, case):
        final_res = Result(case)

        random.seed(time.time())

        tests = 4*(10**3)
        names = ["andrew", "barney", "cassandra", "daniella", "estoban", "felix", "gill", "holly", "ivan", "jackson", "karissa", "leonie", "marcus", "nubert", "olivia", "priscilla", "qname", "raymond", "stacy", "tiff", "uldren", "veronica", "willis", "xander", "yesilda", "zzz", "jab", "proasf", "asdxc", "zpo", "zod"]
        res = [["left" if random.random() < 0.5 else "right" for _ in range(15)] for _ in range(tests)]
        name_actual = []
        for _ in range(tests):
            random.shuffle(names)
            name_actual.append(names[:16])
        
        ans = []
        for x in range(15):

            self._launch_process(case)
            
            inp = str(tests) + "\n"
            for y in range(tests):
                inp = inp + "\n".join(f"{name_actual[y][z]} has the defuser button on the {res[y][z]}" for z in range(15) if z != x) + f"\nYour name is {name_actual[y][x]}\n"

            error = self._interact_with_process(case, final_res, inp.encode("utf-8"))

            process = self._current_proc

            self.populate_result(error, final_res, process)

            output = final_res.proc_output

            if error:
                final_res.result_flag = Result.RTE
                final_res.proc_output = "Your program produced an error."
                return final_res

            try:
                o = output.decode().strip().split()
                assert len(o) == tests
                for x in o:
                    assert x in ['left', 'right', 'pass']
                ans.append(o)
            except:
                final_res.result_flag = Result.WA
                final_res.proc_output = f"Program did not give output that was {tests} lines with `left` `right` or `pass`."
                return final_res

        survived = tests
        for c in range(tests):
            bad = False
            answered_good = False
            for x in range(15):
                if ans[x][c] == "pass": continue
                if ans[x][c] == res[c][x]:
                    answered_good = True
                else:
                    bad = True
                    break
            if bad or not answered_good:
                survived -= 1

        print(survived, tests, file=sys.stderr)

        if survived / tests >= 0.9:
            final_res.result_flag = Result.AC
            final_res.proc_output = "Correct!"
            final_res.points = case.points
        else:
            final_res.result_flag = Result.WA
            final_res.proc_output = f"You only survived {survived/tests*100:.2f}% of cases"

        return final_res
