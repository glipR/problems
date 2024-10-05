import itertools
from collections import deque

t = int(input())

hand_size = 6
num_values = 6
res = 1
for x in range(hand_size + 1, hand_size + num_values):
    res *= x
for x in range(1, num_values):
    res //= x
# res = (handsize + numvalues - 1) choose (handsize)
counts = [0] * res * num_values

# Precompute the possible winning/losing locations.
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
    m[tuple(counts[i*num_values:i*num_values+num_values])] = i

# 0 = DEAL
# 1 = WIN
# -1 = LOSE
CURRENT_STATUS = [0] * (res * res)
DEG = [0] * (res * res)

# Now, any vertex is just two numbers, ranging from 0 to res-1.
# We assume for a particular node that it is my turn.
# Then in the recursion we simply invert at each opportunity.
decided_queue = deque()
win_index = m[(1, 1, 1, 1, 1, 1)]
for i in range(res):
    if i != win_index:
        decided_queue.append(win_index * res + i)
        CURRENT_STATUS[win_index * res + i] = 1
        decided_queue.append(i * res + win_index)
        CURRENT_STATUS[i * res + win_index] = -1

for i in range(res * res):
    id1 = i // res
    id2 = i % res
    # What choices can I make as id1?
    l_options = 0
    for x in range(num_values):
        if counts[id1 * num_values + x] > 0:
            # We could pick x
            l_options += 1
    # We can always pick the wild marble.
    r_options = 1
    for y in range(num_values):
        if counts[id2 * num_values + y] > 0:
            # We could pick y
            r_options += 1
    DEG[i] = l_options * r_options

p = [False] * (res * res)
parent = [-1] * (res * res)

rev = [4, 5, 3, 2, 0, 1]

while len(decided_queue) > 0:
    index = decided_queue.pop()
    if p[index]:
        raise ValueError("Cycle bad.")
    p[index] = True
    # Check all possible inroads to this state.
    # Which of the marbles could've p2 just picked?
    id1 = index // res
    id2 = index % res
    # Loop over the possible choices we could've made.
    for x in range(num_values):
        if counts[id2 * num_values + x] > 0:
            # What if p2 picked x?
            # Well, if it was wild, then everything else needs to rotate.
            n_count = [counts[id2 * num_values + ((i + 1) % num_values)] for i in range(num_values)]
            n_count[x] += 1
            n_count[(x-1) % num_values] -= 1
            old_id2 = m[tuple(n_count)]
            old_index = old_id2 * res + id1
            if CURRENT_STATUS[old_index] == 0:
                DEG[old_index] -= 1
                if CURRENT_STATUS[index] == -1:
                    # If the other player is winning here, they can move here to win.
                    CURRENT_STATUS[old_index] = 1
                    decided_queue.append(old_index)
                    parent[old_index] = index
                else:
                    if DEG[old_index] == 0:
                        # We've tried every edge and all of them are winning for me, so losing for the person above.
                        CURRENT_STATUS[old_index] = -1
                        decided_queue.append(old_index)
                        parent[old_index] = index
            # Otherwise, we could've picked the reverse colour on p1.
            if counts[id1 * num_values + rev[x]] > 0:
                # We could've picked that marble from p1. But what did we come from?
                for y in range(num_values):
                    n_count = [counts[id2 * num_values + i] for i in range(num_values)]
                    n_count[x] -= 1
                    n_count[y] += 1
                    old_id2 = m[tuple(n_count)]
                    old_index = old_id2 * res + id1
                    if CURRENT_STATUS[old_index] == 0:
                        DEG[old_index] -= 1
                        if CURRENT_STATUS[index] == -1:
                            # If the other player is winning here, they can move here to win.
                            CURRENT_STATUS[old_index] = 1
                            decided_queue.append(old_index)
                            parent[old_index] = index
                        else:
                            if DEG[old_index] == 0:
                                # We've tried every edge and all of them are winning for me, so losing for the person above.
                                CURRENT_STATUS[old_index] = -1
                                decided_queue.append(old_index)
                                parent[old_index] = index

marble_map = {
    v: i
    for i, v in enumerate("RBYPGO")
}

for case in range(t):
    start = input()
    Jessica_hand = input().split()
    c = [0] * num_values
    for h in Jessica_hand:
        if h != "W":
            c[marble_map[h]] += 1
    Jessica = m[tuple(c)]
    Arjun_hand = input().split()
    c = [0] * num_values
    for h in Arjun_hand:
        if h != "W":
            c[marble_map[h]] += 1
    Arjun = m[tuple(c)]
    if start == "Jessica":
        index = Jessica * res + Arjun
        if CURRENT_STATUS[index] == 0:
            print("Stalemate")
        elif CURRENT_STATUS[index] == 1:
            print("Jessica")
        else:
            print("Arjun")
    else:
        index = Arjun * res + Jessica
        if CURRENT_STATUS[index] == 0:
            print("Stalemate")
        elif CURRENT_STATUS[index] == 1:
            print("Arjun")
        else:
            print("Jessica")
