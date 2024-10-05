t = int(input())

class Card:
    V_MAP = {
        "2":0,
        "3":1,
        "4":2,
        "5":3,
        "6":4,
        "7":5,
        "8":6,
        "9":7,
        "T":8,
        "J":9,
        "Q":10,
        "K":11,
        "A":12,
    }
    S_MAP = {
        "D": 0,
        "C": 1,
        "H": 2,
        "S": 3,
    }

    def __init__(self, s) -> None:
        self.s = s[0]
        self.s_i = self.S_MAP[self.s]
        self.v = s[1]
        self.i_v = self.V_MAP[self.v]

    def __lt__(self, o):
        return (self.i_v < o.i_v) if self.i_v != o.i_v else self.s_i < o.s_i

    def __lte__(self, o):
        return self.i_v <= o.i_v if self.i_v != o.i_v else self.s_i <= o.s_i

def best_hand(hand):
    # First, check for a 4 of a kind
    counts = {}
    for c in hand:
        if c.i_v not in counts:
            counts[c.i_v] = 0
        counts[c.i_v] += 1
    for key in counts:
        if counts[key] == 4:
            return 7
    # Next, check for a full house
    c3, c2 = False, False
    for key in counts:
        if counts[key] == 3:
            c3 = True
        if counts[key] == 2:
            c2 = True
    if c2 and c3:
        return 6
    # Next, check for a straight
    sorted_h = sorted(hand)
    for start in range(len(sorted_h)):
        v = sorted_h[start].i_v
        for x in range(1, len(sorted_h)):
            if sorted_h[(start + x) % len(sorted_h)].i_v != (v + x) % 13:
                break
        else:
            return 5
    # Next, check for a flush
    if len(set(map(lambda c: c.s, hand))) == 1:
        return 4
    # Next, check for a three of a kind
    if c3:
        return 3
    # Next, two pairs
    n_p = 0
    for key in counts:
        if counts[key] == 2:
            n_p += 1
    if n_p == 2:
        return 2
    if n_p == 1:
        return 1
    return 0



for case in range(t):

    p1hand = list(map(Card, input().split()))
    p2hand = list(map(Card, input().split()))

    t1 = best_hand(p1hand)
    t2 = best_hand(p2hand)

    if t1 > t2 or t1 == t2 and max(p1hand) > max(p2hand):
        print("Belinda")
    else:
        print("Joey")
