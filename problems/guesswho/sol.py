import time
from collections import defaultdict
n, f = list(map(int, input().split()))

features = [input() for _ in range(f)]
characters = [input().split() for _ in range(n)]

import sys
print(features, characters, file=sys.stderr)

possible = [True]*n
while sum(possible) > 1:
    s = sum(possible)
    # Count how many occurrences of each feature value
    value_count = [defaultdict(lambda: 0) for _ in range(f)]
    for i, character in enumerate(characters):
        if not possible[i]: continue
        for x in range(f):
            value_count[x][character[x]] += 1
    best_choice = (None, None, -1)
    # Find the best query to split the remaining characters
    for x in range(f):
        for key in value_count[x]:
            frac = value_count[x][key] / s
            frac = min(frac, 1 - frac)
            if frac > best_choice[2]:
                best_choice = (x, key, frac)
    print(f"QUERY {features[best_choice[0]]} = {best_choice[1]}")
    res = input()
    if res == "YES":
        for x in range(n):
            if not possible[x]: continue
            if characters[x][best_choice[0]] != best_choice[1]:
                possible[x] = False
    elif res == "NO":
        for x in range(n):
            if not possible[x]: continue
            if characters[x][best_choice[0]] == best_choice[1]:
                possible[x] = False

for x in range(n):
    if possible[x]:
        print(f"GUESS {x+1}")
