queues, k, max_val = list(map(int, input().split()))

vals = []
for queue in range(1, queues+1):
    for i in range(1, k+1):
        print(f"VAL {queue} {i}")
        vals.append((int(input()), queue, i))
vals.sort()
print(f"ANS {vals[k-1][1]} {vals[k-1][2]}")
