import heapq

growth, P, E = list(map(int, input().split()))
initial_heights = list(map(int, input().split()))

events = [
    list(map(int, input().split()))
    for _ in range(E)
]

def height_from_weight(day, weight):
    return -weight + growth * day

def weight_from_height(day, height):
    return -(height - growth * day)

poppies = [weight_from_height(0, p) for p in initial_heights]
heapq.heapify(poppies)

for ev in events:
    day = ev[0]
    if ev[1] == 0:
        # Harvest
        poppy = heapq.heappop(poppies)
        print(height_from_weight(day, poppy))
    elif ev[1] == 1:
        # Plant
        height = ev[2]
        heapq.heappush(poppies, weight_from_height(day, height))
    else:
        raise ValueError()
