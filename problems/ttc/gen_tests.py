import string
import random

max_val = 2 * pow(10, 5)
max_time = pow(10, 9)

test_set_num = {}
def write_test(set_num, contents):
    if type(set_num) == list:
        for num in set_num:
            write_test(num, contents)
        return
    if set_num not in test_set_num:
        test_set_num[set_num] = 0
    test_set_num[set_num] += 1
    with open(f"tests/{set_num}_{test_set_num[set_num]}.in", "w") as f:
        f.write(contents)

def rand_name():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))

names = set()
while len(names) < 3 * max_val:
    names.add(rand_name())
names = list(names)

write_test(0, """\
4 8
CityA ArmyA
CityB ArmyB
CityC ArmyC
CityD ArmyB
DEFENDER CityA
ATTACK ArmyA ArmyB 1010
ATTACK ArmyC ArmyA 1015
DEFENDER CityB
RESET 1010
DEFENDER CityD
ATTACK ArmyA ArmyC 1015
DEFENDER CityC""")

for set_num in range(1, 3):
    # Some edge cases
    # Resetting past previous reset
    write_test(set_num, """\
4 13
CityA ArmyA
CityB ArmyB
CityC ArmyC
CityD ArmyD
ATTACK ArmyB ArmyA 10
ATTACK ArmyC ArmyD 15
DEFENDER CityB
DEFENDER CityD
RESET 10
DEFENDER CityD
ATTACK ArmyD ArmyB 15
DEFENDER CityB
RESET 5
DEFENDER CityA
ATTACK ArmyD ArmyA 10
DEFENDER CityA
DEFENDER CityB
""")

    # Resetting nothing
    write_test(set_num, """\
4 7
CityA ArmyA
CityB ArmyB
CityC ArmyC
CityD ArmyD
RESET 5
ATTACK ArmyA ArmyB 10
RESET 15
DEFENDER CityB
RESET 9
ATTACK ArmyB ArmyA 10
DEFENDER CityA
""")

    # Back to back resets
    write_test(set_num, """\
4 9
CityA ArmyA
CityB ArmyB
CityC ArmyC
CityD ArmyD
ATTACK ArmyA ArmyB 10
ATTACK ArmyC ArmyA 15
DEFENDER CityB
RESET 13
DEFENDER CityB
RESET 5
DEFENDER CityB
ATTACK ArmyB ArmyC 20
DEFENDER CityC
""")

    # Long string of attacks
    random.shuffle(names)
    amount = max_val // 3
    armies = names[:amount]
    cities = names[amount:2*amount]
    actions = [
        f"ATTACK {armies[i]} {armies[i-1]} {20*i}"
        for i in range(1, amount)
    ]
    actions.extend([
        f"DEFENDER {cities[i]}"
        for i in range(amount)
    ])
    action_str = "\n".join(actions)
    city_defns = "\n".join(f"{cities[i]} {armies[i]}" for i in range(amount))
    write_test(set_num, f"""\
{amount} {len(actions)}
{city_defns}
{action_str}
""")

    # Semi long str with resets.
    random.shuffle(names)
    n_resets = 3
    amount = max_val // (3 * (n_resets + 1))
    armies = names[:amount]
    cities = names[amount:2*amount]
    actions = []
    for j in range(n_resets+1):
        actions = [
            f"ATTACK {armies[i]} {armies[i-1]} {20*i}"
            for i in range(1, amount)
        ]
        actions.extend([
            f"DEFENDER {cities[i]}"
            for i in (
                range(amount-1, -1, -1)
                if j % 2 == 0 else
                range(amount)
            )
        ])
        if j != n_resets:
            actions.append("RESET 1")
    action_str = "\n".join(actions)
    city_defns = "\n".join(f"{cities[i]} {armies[i]}" for i in range(amount))
    write_test(set_num, f"""\
{amount} {len(actions)}
{city_defns}
{action_str}
""")

def random_test(set_num, limit_resets, attack_chance=0.5, defender_chance=0.4, reset_chance=0.1):
    cities = random.randint(max_val // 2, max_val)
    armies = random.randint(cities // 2, cities)
    random.shuffle(names)
    city_names = names[:cities]
    army_names = names[cities:cities + armies]
    assoc = [random.choice(army_names) for _ in range(cities)]
    selected = set()
    for army in assoc:
        selected.add(army)
    army_names = list(selected)
    n_queries = random.randint(max_val // 2, max_val)
    if limit_resets:
        reset_chance = 5 / n_queries
        amount_reset = 0

    city_defn = "\n".join(f"{city_names[i]} {assoc[i]}" for i in range(cities))

    cur_time = 1
    not_lost = set(army_names)
    battle_stack = []

    queries = []
    for testing_num in range(n_queries):
        total = defender_chance
        can_reset = (not limit_resets) or amount_reset < 5
        can_attack = len(not_lost) >= 2
        total += reset_chance * can_reset
        total += attack_chance * can_attack

        rand = random.random() * total
        rand -= attack_chance * can_attack
        if rand <= 0:
            # Attacking. Select two armies that haven't lost yet
            def random_army():
                if len(not_lost) < 500:
                    return random.choice(list(not_lost))
                else:
                    while True:
                        attempt = random.choice(army_names)
                        if attempt in not_lost:
                            return attempt
            army1 = random_army()
            army2 = army1
            while army2 == army1:
                army2 = random_army()
            time = random.randint(max(cur_time, 2), min(max_time, cur_time + 50))
            queries.append(f"ATTACK {army1} {army2} {time}")
            cur_time = time
            battle_stack.append((army1, army2, time))
            not_lost.remove(army2)
            continue
        rand -= defender_chance
        if rand <= 0:
            # Defender check. Select a random city
            queries.append(f"DEFENDER {random.choice(city_names)}")
            continue
        rand -= reset_chance * can_reset
        if rand <= 0:
            # Reset. Pick a point in the battle stack to reset to.
            # This will make the battle_stack[:ind]
            ind = random.randint(0, len(battle_stack))
            while 0 < ind < len(battle_stack) and battle_stack[ind-1][2] == battle_stack[ind][2]:
                ind += 1 # Can't split if they are on the same year.
            last_time = max_time+1
            for i in range(len(battle_stack)-1, ind-1, -1):
                army1, army2, time = battle_stack.pop()
                not_lost.add(army2)
                last_time = time
            if len(battle_stack) == 0:
                prev_time = 1
            else:
                prev_time = battle_stack[-1][2]
            new_time = random.randint(prev_time, last_time-1)
            queries.append(f"RESET {new_time}")
            cur_time = new_time
            if limit_resets:
                amount_reset += 1
    query_text = "\n".join(queries)
    write_test(set_num, f"""\
{cities} {n_queries}
{city_defn}
{query_text}
""")

for _ in range(5):
    random_test(1, True)

for _ in range(5):
    random_test(2, False)
