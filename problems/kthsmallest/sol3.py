from heapq import heapify, heappop, heappush

queues, k, max_val = list(map(int, input().split()))

vals = []
heapify(vals)

amount_seen = 0
for queue in range(1, queues + 1):
    print(f"VAL {queue} {1}")
    heappush(vals, (int(input()), queue, 1))

while amount_seen < k:
    val, queue, i = heappop(vals)
    amount_seen += 1
    print(f"VAL {queue} {i+1}")
    heappush(vals, (int(input()), queue, i+1))
print(f"ANS {queue} {i}")
