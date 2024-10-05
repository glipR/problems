nbirds, nsounds = list(map(int, input().split()))

bird_sounds = [(lambda x: (int(x[0]), int(x[1]), x[2]) )(input().split()) for _ in range(nbirds)]

total_sounds = []
for i, (start, freq, sound) in enumerate(bird_sounds):
    for index in range(nsounds):
        # Include i to ensure stable sorting.
        total_sounds.append((start + freq * index, i, sound))
total_sounds.sort()
total_sounds = total_sounds[:nsounds]
for _, _, sound in total_sounds:
    print(sound)
