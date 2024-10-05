import random

with open("tests/1.in", "w") as f:
    f.write("""\
4 4 12
1 4
1 1
1 3
3 3
3 4
3 1
2 2
2 4
2 1
4 2
4 3
4 1
""")

with open("tests/2.in", "w") as f:
    f.write("""\
1 1 1
1 1
""")

with open("tests/3.in", "w") as f:
    f.write("""\
2 2 0
""")

# Cats work dogs don't    
with open("tests/4.in", "w") as f:
    f.write("""\
2 3 4
1 2
1 1
2 1
2 2
""")

# Dogs work cats don't    
with open("tests/5.in", "w") as f:
    f.write("""\
3 2 4
1 2
1 1
2 1
2 2
""")

MAX_CATS = 3000
MAX_CONNECTIONS = 50000

for tno in range(6, 11):
    n_cats = random.randint(MAX_CATS//4, MAX_CATS)
    n_dogs = n_cats
    
    pairing_chance = MAX_CONNECTIONS / n_cats / n_cats
    pairings = []
    for x in range(n_cats):
        for y in range(n_dogs):
            if random.random() < pairing_chance:
                pairings.append((x+1, y+1))
    random.shuffle(pairings)
    pairings = pairings[:MAX_CONNECTIONS]
    
    with open(f"tests/{tno}.in", "w") as f:
        f.write(f"{n_cats} {n_dogs} {len(pairings)}\n" + "\n".join(
            f"{x[0]} {x[1]}" for x in pairings
        ))
