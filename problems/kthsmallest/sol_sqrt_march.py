import sys
import math
from heapq import heapify, heappop, heappush

queues, k, max_val = list(map(int, input().split()))

march_step = max(1, math.floor(math.sqrt(k/queues)))
print("fil", queues, k, march_step, file=sys.stderr)

vals = []
heapify(vals)

popped = []

amount_fixed = 0
for queue in range(1, queues + 1):
    print(f"VAL {queue} {march_step}")
    v = int(input())
    # print(queue, march_step, v, file=sys.stderr)
    heappush(vals, (v, queue, march_step))

fixed_pos = [0]*queues
while amount_fixed + march_step <= k - (queues-1) * (march_step-1):
    val, queue, i = heappop(vals)
    popped.append((val, queue, i))
    fixed_pos[queue-1] = i
    amount_fixed += march_step
    print(f"VAL {queue} {i+march_step}")
    v = int(input())
    # print(queue, i+march_step, v, file=sys.stderr)
    heappush(vals, (v, queue, i+march_step))

# Fixed as many as we can with march_step
new_vals = []
heapify(new_vals)

for queue in range(1, queues + 1):
    print(f"VAL {queue} {fixed_pos[queue-1]+1}")
    v = int(input())
    # print(queue, fixed_pos[queue-1]+1, v, file=sys.stderr)
    heappush(new_vals, (v, queue, fixed_pos[queue-1]+1))

while amount_fixed < k:
    val, queue, i = heappop(new_vals)
    popped.append((val, queue, i))
    amount_fixed += 1
    print(f"VAL {queue} {i+1}")
    v = int(input())
    # print(queue, i+1, v, file=sys.stderr)
    heappush(new_vals, (v, queue, i+1))

# print(popped, file=sys.stderr)
last_popped = max(popped)
# print(last_popped[1], last_popped[2], last_popped[0], file=sys.stderr)
print(f"ANS {last_popped[1]} {last_popped[2]}")
