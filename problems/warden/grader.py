import sys
from dmoj.graders import StandardGrader
from dmoj.result import Result

class Grader(StandardGrader):
    def grade(self, case):
        res = Result(case)

        current_state = case.input_data().split()[0].decode()
        position = int(case.input_data().split()[1])

        self._launch_process(case)

        error = self._interact_with_process(case, res, ("0\n" + case.input_data().decode()).encode("utf-8"))

        process = self._current_proc

        self.populate_result(error, res, process)

        output = res.proc_output

        if error:
            res.result_flag = Result.RTE
            res.proc_output = "First prisoner encountered a run time error."
            return res

        try:
            o = int(output.decode())
            assert 1 <= o <= 8
            current_state = list(current_state)
            current_state[o-1] = "x" if current_state[o-1] == "o" else "o"
            current_state = "".join(current_state)
        except:
            res.result_flag = Result.WA
            res.proc_output = "First gave output that was not a number from 1-8."
        else:
            self._launch_process(case)

            error = self._interact_with_process(case, res, ("1\n" + current_state + "\n").encode("utf-8"))

            process = self._current_proc

            self.populate_result(error, res, process)
            output2 = res.proc_output

            if error:
                res.result_flag = Result.RTE
                res.proc_output = "Second prisoner encountered a run time error."
                return res

            try:
                o2 = int(output2.decode())

                if o2 == position:
                    res.result_flag = Result.AC
                    res.proc_output = "Correct!"
                    res.points = case.points
                else:
                    res.result_flag = Result.WA
                    res.proc_output = "Second prisoner answered incorrectly."
            except:
                res.result_flag = Result.WA
                res.proc_output = "Second gave output that was not a number from 1-8."

        return res