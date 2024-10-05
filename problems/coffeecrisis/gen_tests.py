import random
DAY, DURATION, STRENGTH, CAFFEINE = range(4)

# Sample
with open("tests/1.in", "w") as f:
    f.write("""\
30 4
6 12 20 14
19 12 10 100
13 8 20 30
3 10 20 4
""")

# Boundary: Some coffee not worth taking
with open("tests/2.in", "w") as f:
    f.write("""\
100 5
5 30 3 22
14 10 300 30
40 3 100 20
48 50 20 1
69 50 20 1
""")

# Boundary: Empty solution, caffiene makes coffee not worth taking over abstaining.
with open("tests/3.in", "w") as f:
    f.write("""\
100 1
20 5 3 85
""")

MAX_DAYS = pow(10, 9)
MAX_COFFEE = pow(10, 5)
MAX_DURATION = pow(10, 9)
MAX_STRENGTH = pow(10, 3)
MAX_CAFFIENE = pow(10, 9)

# Different characteristics for coffee duration coverage.
sparse = lambda d, n: (d // n) * 0.5
normal = lambda d, n: (d // n) * 2
heavy = lambda d, n: (d // n) * 10

selections = [sparse, normal, heavy]

# Large random cases
for x in range(4, 11):
    d = random.randint(MAX_DAYS//2, MAX_DAYS)
    n = random.randint(MAX_COFFEE//2, MAX_COFFEE)
    average_coffee_duration = random.choice(selections)(d, n)
    start_times = list(sorted([random.randint(1, d - n + 1) for _ in range(n)]))
    start_times = [s + i for i, s in enumerate(start_times)]
    coffees = []
    for i in range(n):
        duration = min(random.randint(average_coffee_duration//4,7*average_coffee_duration//4), MAX_DURATION)
        caffeine = min(random.randint(duration//2, 3*duration//2), MAX_CAFFIENE)
        coffees.append([
            start_times[i],
            duration,
            random.randint(1, MAX_STRENGTH),
            caffeine,
        ])
    random.shuffle(coffees)
    coffee_string = "\n".join([" ".join(map(str, a)) for a in coffees])
    with open(f"tests/{x}.in", "w") as f:
        f.write(f"{d} {n}\n{coffee_string}")
