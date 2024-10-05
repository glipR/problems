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

create_case(0, """7
hisss
triiilll
buuurrrbllle
his
trlll
burbble
hello""")

def random_case(n) -> str:
    alph = "abcdefghijklmnopqrstuvwxyz"
    tests = random.randint(n, 100)
    l = list()
    s = ""
    for _ in range(tests):
        if random.random() < 0.5:
            # Hiss
            s = "hi" + ("s" * random.randint(2, 50))
            if random.random() < 0.5:
                # Bad.
                if random.random() < 0.3:
                    # Bad character
                    idx = random.randint(0, len(s) - 1)
                    s = s[:idx] + random.choice(alph) + s[idx + 1:]
                elif random.random() < 0.5:
                    # Extra character
                    s = s + random.choice(alph)
                else:
                    # Not enough characters
                    s = "his" if random.random() < 0.5 else "hss"
        elif random.random() < 0.6:
            # trill
            s = "tr" + ("i" * random.randint(1, 30)) + ("l" * random.randint(2, 30))
            if random.random() < 0.5:
                # Bad.
                if random.random() < 0.3:
                    # Bad character
                    idx = random.randint(0, len(s) - 1)
                    s = s[:idx] + random.choice(alph) + s[idx + 1:]
                elif random.random() < 0.5:
                    # Extra character
                    s = s + random.choice(alph)
                else:
                    # Not enough characters
                    s = "trll" if random.random() < 0.5 else "tril"
        elif random.random() < 0.8:
            # Burble
            s = "b" + ("u" * random.randint(1, 30)) + ("r" * random.randint(1, 30)) + "b" + ("l" * random.randint(1, 24)) + "e"
            if random.random() < 0.5:
                # Bad.
                if random.random() < 0.3:
                    # Bad character
                    idx = random.randint(0, len(s) - 1)
                    s = s[:idx] + random.choice(alph) + s[idx + 1:]
                elif random.random() < 0.5:
                    # Extra character
                    s = s + random.choice(alph)
                else:
                    # Not enough characters
                    s = "brblle" if random.random() < 0.5 else "burbe"
        else:
            s = "".join(random.choice(alph) for __ in range(random.randint(1, 20)))
        if random.random() < 0.2:
            s = "".join(random.choice(alph) for __ in range(random.randint(1, 10))) + s
        if random.random() < 0.3:
            s = "".join(random.choice(alph) for __ in range(random.randint(1, 20)))
        l.append(s)
    return f"{len(l)}\n{'\n'.join(l)}"

for i in range(30):
    create_case(1, random_case(int(i / 30 * 100)))

open("init.yml", "w").write(yaml.dump({"test_cases": subtasks}, indent=2))
