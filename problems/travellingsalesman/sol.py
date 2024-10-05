T = int(input())

for case in range(T):
    n = int(input())
    city_moves = [tuple(map(int, input().split())) for _ in range(n)]
    bad = False
    # First: check that each adjacent movement makes sense.
    for i in range(n):
        if city_moves[i][1] != city_moves[(i+1)%n][0]:
            bad = True
    # Second: check that each city is visited exactly once.
    # This is the same as saying we go in to the city (+1) and out of it (+1) = 2 total mentions.
    counts = [0]*n
    for a, b in city_moves:
        counts[a-1] += 1
        counts[b-1] += 1
    if max(counts) > 2:
        bad = True
    if min(counts) < 2:
        bad = True
    if bad:
        print("BAD")
    else:
        print("GOOD")
