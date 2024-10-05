import math
import subprocess
import sys

q_vals = [
    q for q in range(5, 60, 5)
]

k_vals = [
    k for k in range(5, 300, 30)
] + [
    k for k in range(300, 10000, 800)
]

q_vals = [2, 3, 4, 5] + list(range(10, 31, 3)) + list(range(35, 65, 5)) + list(range(80, 300, 40))
k_vals = list(range(5, 51, 5)) + list(range(100, 1001, 100)) + list(range(1200, 10000, 1000)) + list(range(10000, 100000, 10000)) + list(range(100000, 1000000, 100000))

EXCLUDE_QUERIES = 5000

def linear_excluder(k, q):
    return k * q > EXCLUDE_QUERIES

def march_excluder(k, q):
    return k + q > EXCLUDE_QUERIES

def sqrt_march_excluder(k, q):
    return math.sqrt(k * q) > EXCLUDE_QUERIES

def l2_excluder(k, q):
    return q * math.log2(k) > EXCLUDE_QUERIES

def maxval_excluder(k, q):
    return 20 * q * math.log2(k) > EXCLUDE_QUERIES


def generate_data_points(solution, excluder, max_val=1<<40, n_runs_per_point=5):
    data_points = []
    considered = []
    for q_val in q_vals:
        for k_val in k_vals:

            if excluder(k_val, q_val):
                continue

            considered.append((q_val, k_val))
    for q_val, k_val in considered:
        query_nums = []
        for _ in range(n_runs_per_point):
            proc = subprocess.run(f"py interactive_runner.py py grader.py local -k {k_val} -q {q_val} -v {max_val} -m {EXCLUDE_QUERIES * 3} --exit-queries -- py {solution}", stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            n_queries = proc.returncode
            if n_queries >= 4294967295:
                raise ValueError(f"CRASHED: py interactive_runner.py py grader.py local -k {k_val} -q {q_val} -v {max_val} --exit-queries -- py {solution}")
            query_nums.append(n_queries)

        n_queries = sum(query_nums) / len(query_nums)
        if n_queries >= EXCLUDE_QUERIES * 3:
            print("WARNING: Excluder estimation is off.", file=sys.stderr)
            break

        data_points.append((k_val, q_val, n_queries))
        print(f"sol: {solution}, k:\t{k_val}, q:\t{q_val}, queries:\t{n_queries} Solved: {100 * len(data_points)/len(considered):.2f}%", file=sys.stderr)
    return data_points

solution_file = "sol2"
excluder = maxval_excluder
points = generate_data_points(f"{solution_file}.py", excluder, max_val=1<<20)

with open(f"data_{solution_file}.csv", "w") as f:
    f.write("k, r, Q\n")
    f.writelines(map(lambda x: f"{x[0]}, {x[1]}, {x[2]}\n", points))
