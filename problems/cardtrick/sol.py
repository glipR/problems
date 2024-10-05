from itertools import permutations
person = int(input())

T = int(input())

vals = [
    suit + val
    for suit in "SHDC" for val in "A23456789TJQK"
]

inverse = {
    v: i
    for i, v in enumerate(vals)
}

def possible(c1, c2, c3, c4):
    p = []
    for x in range(52):
        cards = [c1, c2, c3, c4]
        if x in cards: continue
        cards.append(x)
        cards.sort()
        if cards[sum(cards)%5] == x:
            p.append(x)
    return p

permutes = list(permutations(range(4)))

if person == 0:
    # Leanne
    for c in range(T):
        cards = list(map(lambda x: inverse[x], input().split()))
        cards.sort()
        s = sum(cards) % 5
        v = cards[s]
        i = possible(*cards[:s], *cards[s+1:]).index(v)
        p = permutes[i]
        cards.remove(v)
        to_print = []
        for ind in p:
            to_print.append(vals[cards[ind]])
        print(" ".join(to_print))
else:
    # Gerald
    for c in range(T):
        cards = list(map(lambda x: inverse[x], input().split()))
        old_v = cards[:]
        cards.sort()
        p = possible(*cards)
        perm = tuple(cards.index(v) for v in old_v)
        idx = permutes.index(perm)
        print(vals[p[idx]])
