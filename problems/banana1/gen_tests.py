import random
import yaml

random.seed("69")

SUBTASK_POINT_VALUES = [0, 100]
subtasks = [{"batched": [], "points": x} for x in SUBTASK_POINT_VALUES]

def create_case(subtask, input):
    test = len(subtasks[subtask]["batched"])
    subtasks[subtask]["batched"].append({"in" : f"tests/{subtask}_{test}.in","out":f"tests/{subtask}_{test}.out"})
    with open(f"tests/{subtask}_{test}.in","w") as f:
        f.write(input)

create_case(0, """4 6
15
8
31
42""")

def random_case() -> str:
    n = random.randint(1, 10**6)
    c = random.randint(1, 10**2)
    l = [random.randint(1, 10**5) for _ in range(n)]
    return f"{n} {c}\n" + "\n".join(map(str, l))

for i in range(30):
    create_case(1, random_case())

open("init.yml", "w").write(yaml.dump({"test_cases": subtasks}, indent=2))
