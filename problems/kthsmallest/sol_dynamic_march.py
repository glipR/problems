import sys
import math
from heapq import heapify, heappop, heappush

queues, k, max_val = list(map(int, input().split()))


def march(k, q, fixed_pos, popped, jump_size):
    """Changes fixed_pos and popped"""
    vals = []
    heapify(vals)
    for queue in range(1, queues + 1):
        print(f"VAL {queue} {fixed_pos[queue-1] + jump_size}")
        v = int(input())
        heappush(vals, (v, queue, fixed_pos[queue-1] + jump_size))

    amount_fixed = 0

    while amount_fixed + jump_size <= k - (queues-1) * (jump_size-1):
        val, queue, i = heappop(vals)
        popped.append((val, queue, i))
        fixed_pos[queue-1] = i
        amount_fixed += jump_size
        print(f"VAL {queue} {i+jump_size}")
        v = int(input())
        heappush(vals, (v, queue, i+jump_size))

    return amount_fixed

popped = []
fixed_pos = [0]*queues
jump_size = max(1, math.floor(k/queues))
while k:
    print(k, queues, jump_size, file=sys.stderr)
    k -= march(k, queues, fixed_pos, popped, jump_size)
    jump_size = max(1, jump_size // 2)

last_popped = max(popped)
print(f"ANS {last_popped[1]} {last_popped[2]}")
