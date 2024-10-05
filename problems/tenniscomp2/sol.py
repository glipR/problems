competitors = int(input())
names = [input() for _ in range(competitors)]
wins = {n: 0 for n in names}
losses = {n: 0 for n in names}
beats = {n: [] for n in names}
for _ in range(competitors-1):
    player1, _beats, player2 = input().split()
    wins[player1] += 1
    losses[player2] += 1
    beats[player1].append(player2)

cheater = None
max_val = max(wins.values())
for name in names:
    if losses.get(name, 0) == 0 and wins.get(name, 0) != max_val:
        cheater = name
        break
else:
    for name in names:
        if losses.get(name, 0) == 0:
            cheater = name


print(cheater, "must be the cheater")
mwins = max(wins.get(n2) for n2 in beats[cheater])
# Whoever they tampered with must have the most wins.
print("They cheated on 1 games")
for n2 in beats[cheater]:
    if wins[n2] == mwins:
        print(f"{cheater} defeats {n2}")
