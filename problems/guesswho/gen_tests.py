import random
# Sample test:

with open("tests/1.in", "w") as f:
    f.write("""\
4 3
Hair
Eyes
Hat
Brown Blue Cap
Blonde Blue Beanie
Blonde Green None
Grey Brown Beanie
3
""")


FEATURES = {
    "Hair": ["Brown", "Blue", "Blonde", "Green", "Black", "Bald"],
    "Eyes": ["Red", "Blue", "Purple", "Black", "Brown", "Green"],
    "Hat": ["Cap", "Beanie", "Fedora", "None", "Tribly"],
    "Gender": ["Male", "Female", "Other"],
    "Pleeb": ["Blop", "Blap", "Blip", "Blee", "Bleg"],
    "Grak": ["Blop", "Blap", "Blip", "Blee", "Bleg"],
    "Plorb": ["Blop", "Blap", "Blip", "Blee", "Bleg"],
    "Minfl": ["Blop", "Blap", "Blip", "Blee", "Bleg"],
    "Preat": ["Blop", "Blap", "Blip", "Blee", "Bleg"],
    "Krub": ["Blop", "Blap", "Blip", "Blee", "Bleg"],
}

MAX_FEATURES = 4
MAX_OPTIONS = 3

for test in range(2, 11):
    # 2-15, only 4 features, with top 3 options
    n_f = random.randint(MAX_FEATURES//2, MAX_FEATURES)
    n = random.randint(pow(n_f, MAX_OPTIONS)//2, pow(n_f, MAX_OPTIONS))
    features = set()
    while len(features) < n_f:
        features.add(random.choice(list(FEATURES.keys())))
    features = list(features)
    options = {}
    for feature in features:
        n_options = random.randint(MAX_OPTIONS-1, MAX_OPTIONS)
        options[feature] = FEATURES[feature][:n_options]
    characters = [
        [random.choice(options[features[i]]) for i in range(len(features))]
        for _ in range(n)
    ]
    correct = random.randint(0, len(characters)-1)
    to_remove = []
    for x in range(len(characters)):
        if x == correct: continue
        same = True
        for i in range(len(features)):
            if characters[x][i] != characters[correct][i]:
                same = False
                break
        if same:
            to_remove.append(x)
    diff = 0
    for r in to_remove:
        if r < correct:
            diff += 1
    correct -= diff
    for r in to_remove[::-1]:
        del characters[r]
    with open(f"tests/{test}.in", "w") as f:
        f.write(f"{len(characters)} {n_f}\n")
        for feature in features:
            f.write(feature + "\n")
        for character in characters:
            f.write(" ".join(character) + "\n")
        f.write(f"{correct}\n")

MAX_FEATURES = 6
MAX_OPTIONS = 4
for test in range(11, 26):
    # 16-30, 7 features, with top 5 options
    n_f = random.randint(int(MAX_FEATURES*0.7), MAX_FEATURES)
    n = random.randint(pow(n_f, MAX_OPTIONS)//2, pow(n_f, MAX_OPTIONS))
    n = min(n, 1000)
    features = set()
    while len(features) < n_f:
        features.add(random.choice(list(FEATURES.keys())))
    features = list(features)
    options = {}
    for feature in features:
        n_options = random.randint(MAX_OPTIONS-1, MAX_OPTIONS)
        options[feature] = FEATURES[feature][:n_options]
    characters = [
        [random.choice(options[features[i]]) for i in range(len(features))]
        for _ in range(n)
    ]
    correct = random.randint(0, len(characters)-1)
    to_remove = []
    for x in range(len(characters)):
        if x == correct: continue
        same = True
        for i in range(len(features)):
            if characters[x][i] != characters[correct][i]:
                same = False
                break
        if same:
            to_remove.append(x)
    diff = 0
    for r in to_remove:
        if r < correct:
            diff += 1
    correct -= diff
    for r in to_remove[::-1]:
        del characters[r]

    with open(f"tests/{test}.in", "w") as f:
        f.write(f"{len(characters)} {n_f}\n")
        for feature in features:
            f.write(feature + "\n")
        for character in characters:
            f.write(" ".join(character) + "\n")
        f.write(f"{correct}\n")

