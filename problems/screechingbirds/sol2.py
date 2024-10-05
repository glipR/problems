nbirds, nsounds = list(map(int, input().split()))

bird_sounds = [(lambda x: (int(x[0]), int(x[1]), x[2]) )(input().split()) for _ in range(nbirds)]

counters = [
    x[0]
    for x in bird_sounds
]

output = []

sounds = 0
while True:
    if sounds == nsounds:
        break
    for i in range(nbirds):
        if counters[i] == 0:
            counters[i] = bird_sounds[i][1]-1
            output.append(bird_sounds[i][2])
            sounds += 1
            if sounds == nsounds:
                break
        else:
            counters[i] -= 1

print("\n".join(output))