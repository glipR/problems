import math
import random

# Sample 1: Random small sample with nice edge cases.
with open("tests/1.in", "w") as f:
    f.write("""\
2 15
as|s|sda|ds|sw
s|das|ds|s|as
as s|das|ds|s
""")

# Sample 2: No inputs, matching does not span missing frame.
with open("tests/2.in", "w") as f:
    f.write("""\
3 20
aw|a|s|d|w|a
|a|s|d||w|a
w|sw|s||a|s|d|w|d
- a|s|d|w|a""")

# Sample 3: Extra matching from at end of player input.
with open("tests/3.in", "w") as f:
    f.write("""\
2 20
da|a|d||a|d||a||d|
w|a||d||w|a||d|s
ad a||d||a||d
""")

# Edge 4: Matching at beginning of player input. 
# (And check for different characters used to split special word and player inputs)
with open("tests/4.in", "w") as f:
    f.write("""\
2 20
a|s|d|d
a|a|a|s|d|w
- a|s|d|d
""")

# Edge 5: Match occurs after smallest player input.
with open("tests/5.in", "w") as f:
    f.write("""\
2 20
a
d|s|d|wad|dsw|ws||
s wda|wsd|sw||
""")

# Large 1: One big player, with many large substrings
with open("tests/6.in", "w") as f:
    potg_repeat = "as|dw|" * (1000000 // 6)
    player_good = ["sa|wd|","as|wd|", "sa|dw|"]
    player_bad = ["wd|as|", "sa|"]
    player_input = "".join(random.choice(player_good) if random.random() < 0.999 else random.choice(player_bad) for _ in range(1000000 // 6))
    f.write("""\
1 1000000
""" + player_input + f"\n- {potg_repeat}")


def gen_random_state_sets(nstates, char_options="wasd"):
    strings = []
    char_count = {k: 0 for k in char_options}
    for _ in range(nstates):
        strings.append("")
        for char in char_options:
            if random.random() > 0.5:
                strings[-1] = strings[-1] + char
                char_count[char] += 1
    return "|".join(strings), char_count

# Large 2: One big player, with many large susbtrings and a large repeating portion.
with open("tests/7.in", "w") as f:
    res, char_count = gen_random_state_sets(1000)
    potg_string = (res + "|") * (1000000 // (len(res)+1))
    starter = "".join(k for k in "wasd" if char_count[k] % 2 == 1) or "-"
    f.write("""\
1 1000000
""" + potg_string + f"\n{starter} {potg_string}")

# Large 3: Sqrt players, Sqrt strings
with open("tests/8.in", "w") as f:
    potg_repeat = "as|dw|" * (1000000 // 6)
    player_good = ["sa|wd|","as|wd|", "sa|dw|"]
    player_bad = ["wd|as|", "sa|"]
    nplayers = int(math.sqrt(1000000))
    player_inputs = [
        "".join(random.choice(player_good) if random.random() < 0.95 else random.choice(player_bad) for _ in range(1000000 // (6 * nplayers)))
        for _ in range(nplayers)
    ]
    f.write(f"{nplayers} 1000000\n" + "\n".join(player_inputs) + f"\n- {potg_repeat}")

# Large 4: Many players
with open("tests/9.in", "w") as f:
    potg_repeat = "as|dw|" * (1000000 // 6)
    player_good = ["sa|wd|","as|wd|", "sa|dw|"]
    player_bad = ["wd|as|", "sa|"]
    nplayers = 10000
    player_inputs = [
        "".join(random.choice(player_good) if random.random() < 0.4 else random.choice(player_bad) for _ in range(1000000 // (6 * nplayers)))
        for _ in range(nplayers)
    ]
    f.write(f"{nplayers} 1000000\n" + "\n".join(player_inputs) + f"\n- {potg_repeat}")

# Random ones small players and low matching
with open("tests/10.in", "w") as f:
    potg, char_count = gen_random_state_sets(1000000 // 5)
    total_length = 1000000
    nplayers = 10
    indicies = list(sorted([random.randint(0, 1000000 - nplayers) for _ in range(nplayers-1)]))
    # Ensure distinct
    indicies = [0] + [x + i + 1 for i, x in enumerate(indicies)] + [1000000]
    player_moves = [
        gen_random_state_sets(end - start)[0] for start, end in zip(indicies[:-1], indicies[1:])
    ]
    starter = "".join(k for k in "wasd" if random.random() > 0.5) or "-"
    player_move_combined = '\n'.join(player_moves)
    f.write(f"{nplayers} 1000000\n{player_move_combined}\n{starter} {potg}")

# Random ones small players and high matching
with open("tests/11.in", "w") as f:
    potg, char_count = gen_random_state_sets(1000000 // 5, "a")
    total_length = 1000000
    nplayers = 10
    indicies = list(sorted([random.randint(0, 1000000 - nplayers) for _ in range(nplayers-1)]))
    # Ensure distinct
    indicies = [0] + [x + i + 1 for i, x in enumerate(indicies)] + [1000000]
    player_moves = [
        gen_random_state_sets(end - start, "a")[0] for start, end in zip(indicies[:-1], indicies[1:])
    ]
    starter = "".join(k for k in "a" if random.random() > 0.5) or "-"
    player_move_combined = '\n'.join(player_moves)
    f.write(f"{nplayers} 1000000\n{player_move_combined}\n{starter} {potg}")

# Random ones large players and high matching
with open("tests/12.in", "w") as f:
    potg, char_count = gen_random_state_sets(1000000 // 5, "aw")
    total_length = 1000000
    nplayers = 1000
    indicies = list(sorted([random.randint(0, 1000000 - nplayers) for _ in range(nplayers-1)]))
    # Ensure distinct
    indicies = [0] + [x + i + 1 for i, x in enumerate(indicies)] + [1000000]
    player_moves = [
        gen_random_state_sets(end - start, "aw")[0] for start, end in zip(indicies[:-1], indicies[1:])
    ]
    starter = "".join(k for k in "aw" if random.random() > 0.5) or "-"
    player_move_combined = '\n'.join(player_moves)
    f.write(f"{nplayers} 1000000\n{player_move_combined}\n{starter} {potg}")
