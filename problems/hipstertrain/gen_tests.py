import random

# Sample
with open("tests/1.in", "w") as f:
    f.write("""\
2 3
1 3 2 50 1
4 4 1 50 0
""")

# 2 - 4, 1000 hipsters.

# Notes:
# - Generator needs to ensure the answer is neither 0 nor #hipsters.
# - Some variance in groupie number is good, but not enough to where one station is superior
# - Some capacity should be added, but juggling existing hipsters is required.
group_size = (1, 15)
leave_pct = (0, 0.2)
filled_pct = (0, 100)

for x in range(2, 5):
    with open(f"tests/{x}.in", "w") as f:
        n_stations = random.randint(50, 100)
        n_hipsters = random.randint(n_stations, 1000)
        # Linearly increase hipster distribution with capacity.
        cuts = [random.randint(0, n_hipsters) for _ in range(n_stations-1)]
        cuts.sort()
        cuts = [0] + cuts + [n_hipsters]
        hipster_count = [cuts[x+1] - cuts[x] for x in range(n_stations)]
        # Capacity should start off small, and grow towards the total number of hipsters. Linear growth seems ok.
        end_capacity = int((0.7 * random.random() + 0.3) * n_hipsters * (group_size[0] + group_size[1]) / 2)
        capacity_cuts = [random.randint(0, end_capacity) for _ in range(n_stations)]
        capacity_cuts.sort()
        capacity_cuts = [0] + capacity_cuts + [end_capacity]
        start_capacity = capacity_cuts[1]
        capacities = [capacity_cuts[x+1] - capacity_cuts[x] for x in range(1, n_stations+1)]
        # Group numbers
        group_numbers = [random.randint(*group_size) for _ in range(n_stations)]
        # Leave
        leave_numbers = [int((leave_pct[0] + random.random() * (leave_pct[1] - leave_pct[0])) * capacity_cuts[i+1]) for i in range(n_stations)]
        # Percentage required - feel like completely random just means that some stations take everyone, and some take noone.
        filled_numbers = [random.randint(*filled_pct) for _ in range(n_stations)]
        # Write
        f.write(f"{n_stations} {start_capacity}\n")
        for x in range(n_stations):
            f.write(f"{capacities[x]} {hipster_count[x]} {leave_numbers[x]} {filled_numbers[x]} {group_numbers[x]}\n")

group_size = (5, 15)
leave_pct = (0, 0.03)
filled_pct = (0, 70)

# 5-10, 10000 hipsters.
for x in range(5, 11):
    with open(f"tests/{x}.in", "w") as f:
        n_stations = random.randint(500, 1000)
        n_hipsters = random.randint(n_stations, 10000)
        # Linearly increase hipster distribution with capacity.
        cuts = [random.randint(0, n_hipsters) for _ in range(n_stations-1)]
        cuts.sort()
        cuts = [0] + cuts + [n_hipsters]
        hipster_count = [cuts[x+1] - cuts[x] for x in range(n_stations)]
        # Capacity should start off small, and grow towards the total number of hipsters. Linear growth seems ok.
        end_capacity = int((0.7 * random.random() + 0.3) * n_hipsters * (group_size[0] + group_size[1]) / 2)
        capacity_cuts = [random.randint(0, end_capacity) for _ in range(n_stations)]
        capacity_cuts.sort()
        capacity_cuts = [0] + capacity_cuts + [end_capacity]
        start_capacity = capacity_cuts[1]
        capacities = [capacity_cuts[x+1] - capacity_cuts[x] for x in range(1, n_stations+1)]
        # Group numbers
        group_numbers = [random.randint(*group_size) for _ in range(n_stations)]
        # Leave
        leave_numbers = [int((leave_pct[0] + random.random() * (leave_pct[1] - leave_pct[0])) * capacity_cuts[i+1]) for i in range(n_stations)]
        # Percentage required - feel like completely random just means that some stations take everyone, and some take noone.
        filled_numbers = [random.randint(*filled_pct) for _ in range(n_stations)]
        # Write
        f.write(f"{n_stations} {start_capacity}\n")
        for x in range(n_stations):
            f.write(f"{capacities[x]} {hipster_count[x]} {leave_numbers[x]} {filled_numbers[x]} {group_numbers[x]}\n")

