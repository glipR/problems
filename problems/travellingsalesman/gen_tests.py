with open("tests/1.in", "w") as f:
    f.write("""\
3
4
4 2
2 1
1 3
3 4
7
1 2
2 3
3 1
1 4
4 5
5 6
6 1
4
1 2
3 2
3 4
1 4""")

import random

for x in range(2, 7):
    with open(f"tests/{x}.in", "w") as f:
        n_tests = random.randint(1, 100)
        f.write(f"{n_tests}\n")
        for _ in range(n_tests):
            n = random.randint(2, 30)
            if random.random() < 0.4:
                # Good
                nums = list(range(1, n+1))
                random.shuffle(nums)
                edges = list(zip(nums, nums[1:] + [nums[0]]))
            elif random.random() < 0.5:
                # Bad - slight change from permutation
                nums = list(range(1, n+1))
                random.shuffle(nums)
                for y in range(3):
                    nums[random.randint(0, n-1)] = random.randint(1, n)
                edges = list(zip(nums, nums[1:] + [nums[0]]))
            else:
                # Bad - edge directions
                nums = list(range(1, n+1))
                random.shuffle(nums)
                edges = list(zip(nums, nums[1:] + [nums[0]]))
                idx = random.randint(0, n-1)
                edges[idx] = (edges[idx][1], edges[idx][0])
            f.write(f"{n}\n")
            for edge in edges:
                f.write(f"{edge[0]} {edge[1]}\n")
