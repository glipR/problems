# Generate some test data.
# TODO: Find a way to generate more interesting cases, or put more points on the final 5 cases.
import random

items = [
    "amulet",
    "sword",
    "axe",
    "armor",
    "poison",
    "dirt",
    "steel",
]

def make_test_case(f, items, rules):
    f.write(f'{len(items)} {len(rules)}\n')
    random.shuffle(items)
    for item in items:
        f.write(item + "\n")
    random.shuffle(rules)
    for i1, m1, i2, m2 in rules:
        n = i1 + ["and"] + [str(m1)] + ["gold", "can", "be", "traded", "for"] + i2 + ["and"] + [str(m2)] + ["gold"]
        f.write(" ".join(n) + "\n")

# Make the sample data 1.in
with open("tests/1.in", "w") as f:
    f.write("""\
2
3 5
sword
axe
armor
and 1 gold can be traded for axe and 0 gold
axe and 2 gold can be traded for sword and 0 gold
axe sword and 3 gold can be traded for armor and 0 gold
sword armor axe and 0 gold can be traded for and 21 gold
armor axe and 0 gold can be traded for armor and 1 gold
2 3
poison
steel
and 1 gold can be traded for poison and 0 gold
poison and 1 gold can be traded for steel and 0 gold
steel and 0 gold can be traded for poison and 1 gold
""")

EASY_POSITIVE_CHANCE = 0.2
EASY_POSITIVE_MULT = 4
EASY_POSITIVE_GIVING_CHANCE = (0.3, 0.5)
EASY_POSITIVE_RECEIVING_CHANCE = 0.03
EASY_NEGATIVE_GIVING_CHANCE = 0.05
EASY_NEGATIVE_RECEIVING_CHANCE = (0.3, 0.5)

# 2 Random cases with n <= 5
for testno in range(2, 4):
    with open(f'tests/{testno}.in', 'w') as f:
        f.write('10\n')
        for _ in range(10):
            n = random.randint(3, 5)
            random.shuffle(items)
            chosen = items[:n]
            rules = []
            n_rules = random.randint(7, 13)
            for i in range(n_rules):
                if EASY_POSITIVE_CHANCE > random.random():
                    # Positive
                    cost_mult = random.random()
                    giv = EASY_POSITIVE_GIVING_CHANCE[0] + EASY_POSITIVE_GIVING_CHANCE[1] * cost_mult
                    weight = int((1 + cost_mult) * EASY_POSITIVE_MULT * 100)
                    giving = [i for i in chosen if random.random() < giv]
                    recving = [i for i in chosen if random.random() < EASY_POSITIVE_RECEIVING_CHANCE]
                    random.shuffle(giving)
                    random.shuffle(recving)
                    diff = int(random.random() * 100)
                    rules.append([
                        giving, diff, recving, weight + diff
                    ])
                else:
                    # Negative
                    cost_mult = random.random()
                    rec = EASY_NEGATIVE_RECEIVING_CHANCE[0] + EASY_NEGATIVE_RECEIVING_CHANCE[1] * cost_mult
                    weight = int((1 + cost_mult) * EASY_NEGATIVE_GIVING_CHANCE * 100)
                    giving = [i for i in chosen if random.random() < EASY_NEGATIVE_GIVING_CHANCE]
                    recving = [i for i in chosen if random.random() < rec]
                    random.shuffle(giving)
                    random.shuffle(recving)
                    diff = int(random.random() * 100)
                    rules.append([
                        giving, weight + diff, recving, diff
                    ])
            make_test_case(f, chosen, rules)

HARD_POSITIVE_CHANCE = 0.05
HARD_POSITIVE_MULT = 6
HARD_POSITIVE_GIVING_CHANCE = (0.3, 0.1)
HARD_POSITIVE_RECEIVING_CHANCE = 0.03
HARD_NEGATIVE_GIVING_CHANCE = 0.1
HARD_NEGATIVE_RECEIVING_CHANCE = (0.1, 0.1)

# 7 random cases with n <= 7
for testno in range(4, 11):
    with open(f'tests/{testno}.in', 'w') as f:
        f.write('10\n')
        for _ in range(10):
            n = random.randint(6, 7)
            random.shuffle(items)
            chosen = items[:n]
            rules = []
            n_rules = random.randint(10, 30)
            for i in range(n_rules):
                if HARD_POSITIVE_CHANCE > random.random():
                    # Positive
                    cost_mult = random.random()
                    giv = HARD_POSITIVE_GIVING_CHANCE[0] + HARD_POSITIVE_GIVING_CHANCE[1] * cost_mult
                    weight = int((1 + cost_mult) * HARD_POSITIVE_MULT * 100)
                    giving = [i for i in chosen if random.random() < giv]
                    recving = [i for i in chosen if random.random() < HARD_POSITIVE_RECEIVING_CHANCE]
                    random.shuffle(giving)
                    random.shuffle(recving)
                    diff = int(random.random() * 100)
                    rules.append([
                        giving, diff, recving, weight + diff
                    ])
                else:
                    # Negative
                    cost_mult = random.random()
                    rec = HARD_NEGATIVE_RECEIVING_CHANCE[0] + HARD_NEGATIVE_RECEIVING_CHANCE[1] * cost_mult
                    weight = int((1 + cost_mult) * HARD_NEGATIVE_GIVING_CHANCE * 100)
                    giving = [i for i in chosen if random.random() < HARD_NEGATIVE_GIVING_CHANCE]
                    recving = [i for i in chosen if random.random() < rec]
                    random.shuffle(giving)
                    random.shuffle(recving)
                    diff = int(random.random() * 100)
                    rules.append([
                        giving, weight + diff, recving, diff
                    ])
            make_test_case(f, chosen, rules)

# Final few tests - hand picked to have longest cycle length.
for testno in range(11, 13):
    with open(f'tests/{testno}.in', 'w') as f:
        f.write('10\n')
        for z in range(10):
            random.shuffle(items)
            using = items[:7]
            rules = []
            total = 0
            for x in range(7):
                c = random.randint(1, 6)
                total += (1 << (6-x)) * c
                rules.append([[using[y] for y in range(x)], c, [using[x]], 0])
            rules.append([using, 0, [], total + random.randint(1, 10)])
            make_test_case(f, items, rules)

# One last test - pretty much the same but a bit less than 128 cycle length
for testno in range(13, 14):
    with open(f'tests/{testno}.in', 'w') as f:
        f.write('10\n')
        for z in range(10):
            random.shuffle(items)
            using = items[:7]
            rules = []
            total = 0
            for x in range(7):
                c = random.randint(1, 6)
                total += (1 << (6-x)) * c
                if random.random() > 0.15:
                    rules.append([[using[y] for y in range(x)], c, [using[x]], 0])
                else:
                    # Get everything back.
                    rules.append([[using[y] for y in range(x)], c, [using[y] for y in range(x+1)], 0])
            rules.append([using, 0, [], total + random.randint(1, 10)])
            make_test_case(f, items, rules)
