import random
import itertools

hand_size = 6
num_values = 6
res = 1
for x in range(hand_size + 1, hand_size + num_values):
    res *= x
for x in range(1, num_values):
    res //= x
# res = (handsize + numvalues - 1) choose (handsize)
counts = [0] * res * num_values

# First, generate the possible hand values, and turn them into integers.
m = {}
for i, v in enumerate(itertools.combinations(range(hand_size + num_values - 1), num_values - 1)):
    prev = -1
    ind = 0
    for x in v:
        counts[i * num_values + ind] = x - prev - 1
        prev = x
        ind += 1
    counts[i * num_values + ind] = hand_size + num_values - prev - 2

mapping = "RBYPGO"

with open("tests/1.in", "w") as f:
    f.write("""\
3
Arjun 
W R B Y P G G
W R R B Y P G
Arjun
R O B B Y W P 
R W R R O O O
Jessica
W B B O R B B
O P G G G W P""")

for x in range(2, 12):
    with open(f"tests/{x}.in", "w") as f:
        n_tests = random.randint(50000, 100000)
        f.write(f"{n_tests}\n")
        for _ in range(n_tests):
            first = random.choice(["Jessica", "Arjun"])
            while True:
                jessica_marbles = random.randint(0, res-1)
                for y in range(num_values):
                    if counts[jessica_marbles * num_values + y] != 1:
                        break
                else:
                    continue
                break
            while True:
                arjun_marbles = random.randint(0, res-1)
                for y in range(num_values):
                    if counts[arjun_marbles * num_values + y] != 1:
                        break
                else:
                    continue
                break
            jessica = ["W"]
            for y in range(num_values):
                if counts[jessica_marbles * num_values + y] != 0:
                    jessica.extend(mapping[y] * counts[jessica_marbles * num_values + y])
            arjun = ["W"]
            for y in range(num_values):
                if counts[arjun_marbles * num_values + y] != 0:
                    arjun.extend(mapping[y] * counts[arjun_marbles * num_values + y])
            random.shuffle(jessica)
            random.shuffle(arjun)
            f.write(f"{first}\n{' '.join(jessica)}\n{' '.join(arjun)}\n")
