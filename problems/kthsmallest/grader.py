import math
import random
import sys
from heapq import heapify, heappop, heappush
from sol1 import solve


def run_with_values(max_k, max_q, max_val, max_queries, interact_fn, interact_read, max_points=1, query_list=[]):
    q = max_q
    generator_bits = math.ceil(math.log2(max_k))
    prev_mult = math.floor(math.pow(max_val, 1/(generator_bits-1)))
    sum_mult = math.floor(math.pow(max_val/generator_bits, 1/(generator_bits-1))) - 1
    print(max_val, prev_mult, sum_mult, file=sys.stderr)
    bit_lists = []
    for _ in range(q):
        bit_list = []
        cur_sum = 0
        prev_bit = 1
        for _ in range(generator_bits+3):
            new_bit = random.randint(max(1, cur_sum), max(prev_mult*prev_bit, sum_mult*cur_sum))
            bit_list.append(new_bit)
            cur_sum += new_bit
            prev_bit = new_bit
        bit_lists.append(bit_list)

    def func(queue_ind, index):
        cur_sum = 0
        for i, bit in enumerate(bit_lists[queue_ind-1]):
            if index & (1 << i):
                cur_sum += bit
        return cur_sum

    if max_k <= 50:
        print("VALS:", [
            [func(queue_ind, i) for i in range(1, max_k+1)]
            for queue_ind in range(1, q+1)
        ], file=sys.stderr)

    k = max_k
    m_val = max(func(i+1, k) for i in range(q))
    if m_val> max_val:
        print("Random Test Generation Failed", file=sys.stderr)

    # Find the kth smallest myself
    res = solve(q, k, m_val, get_val_method=func)

    sol_value, sol_queue, sol_index = func(res[0], res[1]), res[0], res[1]

    print("MAX", m_val, file=sys.stderr)
    interact_fn(f"{q} {k} {m_val}")
    iterations = 0
    while iterations < 3 * max_queries:
        command = interact_read().split()
        iterations += 1
        if len(command) != 3:
            return CheckerResult(False, 0, f"Invalid Interaction: {' '.join(command)}")
        if command[0] == "VAL":
            try:
                queue = int(command[1])
                ind = int(command[2])
            except:
                return CheckerResult(False, 0, f"Invalid Interaction: {' '.join(command)}")
            if ind > k:
                return CheckerResult(False, 0, f"Index Given is larger than k ({k}): {ind}")
            if ind <= 0:
                return CheckerResult(False, 0, f"Index Given is less than 1: {ind}")
            if not (1 <= queue <= q):
                return CheckerResult(False, 0, f"Queue Index Given is not between 1 and {q}: {ind}")
            interact_fn(func(queue, ind))
        elif command[0] == "ANS":
            try:
                queue = int(command[1])
                ind = int(command[2])
            except:
                return CheckerResult(False, 0, f"Invalid Interaction: {' '.join(command)}")
            if ind > k:
                return CheckerResult(False, 0, f"Index Given is larger than k ({k}): {ind}")
            if ind <= 0:
                return CheckerResult(False, 0, f"Index Given is less than 1: {ind}")
            if not (1 <= queue <= q):
                return CheckerResult(False, 0, f"Queue Index Given is not between 1 and {q}: {ind}")
            val = func(queue, ind)
            if val == sol_value:
                print(f"CORRECT! {iterations}", file=sys.stderr)
                if iterations <= max_queries + 1:
                    query_list.append(iterations)
                    return CheckerResult(True, max_points, f"Solved in {iterations} iterations")
                else:
                    return CheckerResult(False, 0, f"Answer provided took too long ({iterations} iterations)")
            else:
                if val < sol_value:
                    return CheckerResult(False, 0, "Answer provided was lesser than the kth smallest.")
                if val > sol_value:
                    return CheckerResult(False, 0, "Answer provided was greater than the kth smallest.")
        else:
            return CheckerResult(False, 0, f"Invalid Command: {' '.join(command)}")
    return CheckerResult(False, 0, "Answer provided took too long")

if not(len(sys.argv) > 1 and sys.argv[1] == "local"):
    from dmoj.graders import InteractiveGrader
    from dmoj.graders.interactive import Interactor
    from dmoj.result import CheckerResult
    from dmoj.problem import TestCase
    class Grader(InteractiveGrader):
        def interact(self, case : TestCase, interactor : Interactor):
            max_q, max_k, max_val = case.input_data().decode("utf-8").split(" ")
            max_q = int(max_q)
            max_k = int(max_k)
            max_val = int(max_val)
            def read():
                return interactor.readln().decode("utf-8")
            result = run_with_values(max_k, max_q, max_val, 3000, interact_fn=interactor.writeln, interact_read=read, max_points=case.points)
            interactor.close()
            return result
else:
    CheckerResult = lambda a, b, c: (a, b, c)

LOCAL_MAX_Q = 5
LOCAL_MAX_K = 300
LOCAL_MAX_VAL = 1 << 10
LOCAL_MAX_QUERIES = 3000

if len(sys.argv) > 1 and sys.argv[1] == "local":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("local")
    parser.add_argument("-k", "--k-val", type=int, default=LOCAL_MAX_K)
    parser.add_argument("-q", "--q-val", type=int, default=LOCAL_MAX_Q)
    parser.add_argument("-v", "--max-val", type=int, default=LOCAL_MAX_VAL)
    parser.add_argument("-m", "--max-queries", type=int, default=3000)
    parser.add_argument("--exit-queries", action="store_true")
    args = parser.parse_args(sys.argv[1:])
    LOCAL_MAX_K = args.k_val
    LOCAL_MAX_Q = args.q_val
    LOCAL_MAX_VAL = args.max_val
    LOCAL_MAX_QUERIES = args.max_queries
    query_list = []
    res = run_with_values(LOCAL_MAX_K, LOCAL_MAX_Q, LOCAL_MAX_VAL, LOCAL_MAX_QUERIES, print, input, query_list=query_list)
    if res[0]:
        if args.exit_queries:
            sys.exit(query_list[0])
        sys.exit(0)
    else:
        print(res[2], file=sys.stderr)
        sys.exit(-1)

