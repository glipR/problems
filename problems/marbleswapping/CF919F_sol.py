# My Solution for CF 919/F.
# AC
import itertools
from collections import deque

t = int(input())

hand_size = 8
num_values = 5
res = 1
for x in range(hand_size + 1, hand_size + num_values):
    res *= x
for x in range(1, num_values):
    res //= x
# res = (handsize + numvalues - 1) choose (handsize)
counts = [0] * res * 5

# Precompute the possible winning/losing locations.
# First, generate the possible hand values, and turn them into integers.
m = {}
for i, v in enumerate(itertools.combinations(range(hand_size + num_values - 1), num_values - 1)):
    prev = -1
    ind = 0
    for x in v:
        counts[i * 5 + ind] = x - prev - 1
        prev = x
        ind += 1
    counts[i * 5 + ind] = hand_size + num_values - prev - 2
    m[tuple(counts[i*5:i*5+5])] = i

# 0 = DEAL
# 1 = WIN
# -1 = LOSE
CURRENT_STATUS = [0] * (res * res)
DEG = [0] * (res * res)

# Now, any vertex is just two numbers, ranging from 0 to res-1.
# We assume for a particular node that it is my turn.
# Then in the recursion we simply invert at each opportunity.
decided_queue = deque()
win_index = m[(hand_size, 0, 0, 0, 0)]
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
    n_options_l = 0
    for x in range(1, 5):
        if counts[id1 * 5 + x] > 0:
            n_options_l += 1
    n_options_r = 0
    for x in range(1, 5):
        if counts[id2 * 5 + x] > 0:
            n_options_r += 1
    DEG[i] = n_options_l * n_options_r

p = [False] * (res * res)
parent = [-1] * (res * res)

while len(decided_queue) > 0:
    index = decided_queue.pop()
    if p[index]:
        raise ValueError("Cycle bad.")
    p[index] = True
    # Check all possible inroads to this state.
    # Which of the cards could've p2 just made?
    id1 = index // res
    id2 = index % res
    for x in range(5):
        if counts[id2 * 5 + x] > 0:
            # We could've made this card.
            # But what would the card have been / what of my cards should they have picked?
            for y in range(1, 5):
                if counts[id1 * 5 + y] > 0:
                    # They could've picked this card.
                    # x = y + z mod 5. So z = x - y mod 5.
                    z = (x - y) % 5
                    if z == 0:
                        continue
                    n_count = [counts[id2 * 5 + i] for i in range(5)]
                    n_count[x] -= 1
                    n_count[z] += 1
                    old_id2 = m[tuple(n_count)]
                    # Remember to flip
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

for case in range(t):
    f = int(input())
    alice_hand = tuple(map(int, input().split()))
    c = [0] * num_values
    for h in alice_hand:
        c[h] += 1
    alice = m[tuple(c)]
    bob_hand = tuple(map(int, input().split()))
    c = [0] * num_values
    for h in bob_hand:
        c[h] += 1
    bob = m[tuple(c)]
    if f == 0:
        index = alice * res + bob
        if CURRENT_STATUS[index] == 0:
            print("Deal")
        elif CURRENT_STATUS[index] == 1:
            print("Alice")
        else:
            print("Bob")
    else:
        index = bob * res + alice
        if CURRENT_STATUS[index] == 0:
            print("Deal")
        elif CURRENT_STATUS[index] == 1:
            print("Bob")
        else:
            print("Alice")
