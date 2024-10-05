Joey and Belinda are playing a card game similar to poker, except the rules are simplified and no betting is included.

Joey and Belinda each get 5 random cards from a standard deck of 52. These cards each have a suit (Spades, Hearts, Clubs or Diamonds) and a face value (ace, two through ten, jack, queen, king). Cards are represented as two character strings. The first is the suit (One of `SHCD`) and the second is the face value (One of `23456789TJQKA`)

Joey or Belinda are trying to get the best hand. The best hand is the one that matches the highest value "special hand".

The special hands, in decreasing order of value is as follows:

* 4 of a kind (Four cards with the same face value). Example: `S4 H4 C4 D4 SA`
* Full house (Three cards with the same face value, and another two cards with the same face value). Example: `S4 H4 C4 CA SA`
* Straight (Five cards that can be ordered so that the face value of the next card is one plus the face value before it, allowing for this to pass the boundary between Ace and King). Example: `C3 SQ DA CK H2`
* Flush (All Five cards have the same suit). Example: `C3 C6 CA C2 C8`
* 3 of a kind (Three cards with the same face value). Example: `S4 H4 C4 SA CK`
* 2 pairs (Two pairs of two cards with the same face value). Example: `S4 H4 SA CA HK`
* 1 pair (Two cards with the same face value). Example: `S4 H4 HA CK SJ`
* Nothing (Any set of 5 cards). Example: `S4 S5 S6 S7 D9`

Note that one hand can be multiple special hands, and in this case we only consider the highest value hand (For example, `S4 H4 C4 CA SA` is a Full house, 3 of a kind, 2 pairs, 1 pair and Nothing hand, but we only consider it a Full house).

The player with the higher value special hand wins. If both players have equal value special hands, then the player with the higher value card wins. A card is higher value if it has higher face value (In order `23456789TJQKA`), or it has equal face value but higher suit (In order `DCHS`). So `SA > SD`.

## Input

Input will being with a single integer ~T~, the number of test cases. ~2T~ lines follow.

Each test case contains 2 lines: One representing Belinda's Hand, and the other representing Joey's Hand.

## Output

For each test case:

* If Belinda wins, print `Belinda`,
* Otherwise, print `Joey`.

## Constraints

* ~1 \leq T \leq 20~.
* Within each test case, each card printed will be unique.

## Sample Run

Input
```
2
ST S4 S7 S9 SK
H3 H4 D2 CA HK
H4 S4 HA SA C4
DJ CJ HJ S2 D2
```

Output
```
Joey
Belinda
```

Explanation: 

* In the first test case, Belinda has a Flush, while Joey has a Straight.
* In the second test case, Both players have a full house, but Belinda highest card is an Ace of Spades, which beats Joey's Jack of Hearts.
