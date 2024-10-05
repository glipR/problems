# competitors is guaranteed to be a power of 2.
competitors = int(input())
stats = {}
cur_stage = []
for _ in range(competitors):
    name, skill_level = input().split()
    skill_level = int(skill_level)
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

print(len(statements))
print("\n".join(statements))
