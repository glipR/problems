import random

with open("tests/1.in", "w") as f:
    f.write("""4
name1
name2
name3
name4
name4 defeats name2
name2 defeats name1
name3 defeats name4
""")

# Edge case - size 2 and winner of comp
with open("tests/2.in", "w") as f:
    f.write("""2
s3
s1
s3 defeats s1
""")


def random_name():
    l = random.randint(5, 20)
    return "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(l)])

def solve_p1(competitors, names, skill_levels):
    # competitors is guaranteed to be a power of 2.
    stats = {}
    cur_stage = []
    for name, skill_level in zip(names, skill_levels):
        stats[name] = skill_level
        cur_stage.append(name)

    statements = []
    while len(cur_stage) > 1:
        new_stage = []
        for x in range(len(cur_stage) // 2):
            t1 = cur_stage[2*x]
            t2 = cur_stage[2*x + 1]
            if (-stats[t1], t1) < (-stats[t2], t2):
                new_stage.append(t1)
                statements.append(f"{t1} defeats {t2}")
            else:
                new_stage.append(t2)
                statements.append(f"{t2} defeats {t1}")
        cur_stage = new_stage

    return statements


competitor_options = [1024, 512, 256]
skill_options = [random.randint(1, pow(10, 9)) for _ in range(700)]
people_names = list(set(random_name() for _ in range(3000)))
# Just random should suffice here.
for x in range(3, 11):
    with open(f"tests/{x}.in", "w") as f:
        competitors = random.choice(competitor_options)
        f.write(f"{competitors}\n")
        random.shuffle(people_names)
        for y in range(competitors):
            f.write(f"{people_names[y]}\n")
        names = people_names[:competitors]
        skill_levels = [random.choice(skill_options) for _ in range(competitors)]
        statements = solve_p1(competitors, names, skill_levels)
        random.shuffle(statements)
        # Pick 1 and flip it.
        index = random.randint(0, len(statements)-1)
        statements[index] = " ".join(statements[index].split(" ")[::-1])
        for statement in statements:
            f.write(statement + "\n")
