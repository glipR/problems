import random

cards = [
    s + v
    for s in "HSDC"
    for v in "A23456789TJQK"
]

# Sample
with open("tests/1.in", "w") as f:
    f.write("""\
2
ST S4 S7 S9 SK
H3 H4 D2 CA HK
H4 S4 HA SA C4
DJ CJ HJ S2 D2
""")

class Deck:

    SUITS = "SHCD"
    VALS = "23456789TJQKA"

    def __init__(self):
        self.cards = {
            c: [s for s in self.SUITS]
            for c in self.VALS
        }
    
    def random_card(self, val=None, suit=None):
        if suit is not None:
            c = random.choice([c for c in self.cards if suit in self.cards[c]])
            self.cards[c].remove(suit)
            return suit + c
        if val is not None:
            possible = [(val, s) for s in self.cards[val]]
        else:
            possible = [(c, s) for c in self.cards for s in self.cards[c]]
        c, s = random.choice(possible)
        self.cards[c].remove(s)
        return s + c

    def count(self, val=None, suit=None):
        if suit is not None:
            return len([c for c in self.cards if suit in self.cards[c]])
        elif val is not None:
            return len(self.cards[val])
        return sum(len(self.cards[c]) for c in self.cards)

truly_random = 0.3

def hand_from_deck(power, deck):
    if power == 1:
        # Ensure we have at least a pair
        while True:
            c = random.choice(deck.VALS)
            if deck.count(val=c) >= 2:
                break
        return [deck.random_card(val=c) for _ in range(2)] + [deck.random_card() for _ in range(3)]
    elif power == 2:
        # Ensure we have two distinct pairs.
        while True:
            c1 = random.choice(deck.VALS)
            c2 = random.choice(deck.VALS)
            if deck.count(val=c1) >= 2 and deck.count(val=c2) >= 2 and c1 != c2:
                break
        return [deck.random_card(val=c1) for _ in range(2)] + [deck.random_card(val=c2) for _ in range(2)] + [deck.random_card()]
    elif power == 3:
        # Ensure we have a 3 of a kind.
        while True:
            c = random.choice(deck.VALS)
            if deck.count(val=c) >= 3:
                break
        return [deck.random_card(val=c) for _ in range(3)] + [deck.random_card() for _ in range(2)]
    elif power == 4:
        # Ensure we have a flush.
        while True:
            s = random.choice(deck.SUITS)
            if deck.count(suit=s) >= 5:
                break
        return [deck.random_card(suit=s) for _ in range(5)]
    elif power == 5:
        # Ensure we have a straight
        while True:
            c_i = random.randint(0, len(deck.VALS) - 1)
            if sum([deck.count(val=deck.VALS[(c_i+i)%len(deck.VALS)]) >= 1 for i in range(5)]) == 5:
                break
        return [deck.random_card(val=deck.VALS[(c_i+i)%len(deck.VALS)]) for i in range(5)]
    elif power == 6:
        # Ensure we have a full house
        while True:
            c1 = random.choice(deck.VALS)
            c2 = random.choice(deck.VALS)
            if deck.count(val=c1) >= 3 and deck.count(val=c2) >= 2 and c1 != c2:
                break
        return [deck.random_card(val=c1) for _ in range(3)] + [deck.random_card(val=c2) for _ in range(2)]
    elif power == 7:
        # Ensure we have a four of a kind
        while True:
            c = random.choice(deck.VALS)
            if deck.count(val=c) >= 4:
                break
        return [deck.random_card(val=c) for _ in range(4)] + [deck.random_card()]


for x in range(2, 10):
    with open(f"tests/{x}.in", "w") as f:
        n_tests = random.randint(5, 20)
        f.write(f"{n_tests}\n")
        for case in range(n_tests):
            d = Deck()
            if random.random() < truly_random:
                c1 = [d.random_card() for _ in range(5)]
                c2 = [d.random_card() for _ in range(5)]
                f.write(" ".join(c1) + "\n")
                f.write(" ".join(c2) + "\n")
            else:
                c1_power = random.randint(1, 7)
                c2_power = random.randint(1, 7)
                c1_hand = hand_from_deck(c1_power, d)
                c2_hand = hand_from_deck(c2_power, d)
                random.shuffle(c1_hand)
                random.shuffle(c2_hand)
                f.write(" ".join(c1_hand) + "\n")
                f.write(" ".join(c2_hand) + "\n")
                
# One final test, with some tricky cases.
with open("tests/10.in", "w") as f:
    # 1: Both straights, but one has a higher card by value.
    # 2: Both full houses, but the triple is highest by value.
    # 3: Both full houses, but the pair is highest by suit.
    f.write("""\
3
SQ HK SJ HA C2
DQ SJ DK CT C9
H4 C4 S4 H5 C5
DJ CJ SJ C2 D2
C4 S4 D4 DQ CQ
D2 C2 H2 SQ HQ
""")
