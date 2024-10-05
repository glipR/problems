with open("tests/1.in", "w") as f:
    f.write("""\
7
roooar
meeeowwwwww
purrrrrr
roaar
pur
rmeow
hello
""")

import random

alph = "abcdefghijklmnopqrstuvwxyz"

for x in range(2, 7):
    with open(f"tests/{x}.in", "w") as f:
        tests = random.randint(1, 20)
        f.write(f"{tests}\n")
        for _ in range(tests):
            if random.random() < 0.3:
                # Meow
                s = "m" + ("e" * random.randint(1, 13)) + "o" + ("w" * random.randint(1, 13))
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
                        s = "mow" if random.random() < 0.5 else "meo"
            elif random.random() < 0.4:
                # Roar
                s = "r" + ("o" * random.randint(1, 22)) + "ar"
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
                        s = "rar" if random.random() < 0.5 else "robr"
            elif random.random() < 0.8:
                # Purr
                s = "pu" + ("r" * random.randint(1, 24))
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
                        s = "pur" if random.random() < 0.5 else "parr"
            else:
                s = "".join(random.choice(alph) for __ in range(random.randint(1, 20)))
            f.write(f"{s}\n")
