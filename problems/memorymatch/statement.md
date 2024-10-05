You and your friend Ernesto are playing a high stakes game at the memory match world finals. Looking cool as ever, you've entered the game wearing some shades indoors 😎. But these aren't any shades, these shades are hooked up to the very code you are about to write!

Memory match is a game where a deck of $2N$ cards, consisting of  $N$ distinct pairs of cards, are shuffled and placed in positions 1 through to $2N$.

You then keep querying two positions,  $a$ and $b$, and those two cards are turned face-up. If they are a pair of the same card, they remain face-up, otherwise the cards are then flipped face-down again. The aim of the game is to have all cards face up **within  $2N$ queries**.

### Interaction

This problem is interactive. Interaction will begin with a single integer $T$, the number of games your program will play.

For each game, the judge will provide a single integer $N$, the number of distinct cards in the deck. Querying can then begin.

To query, simply print two integers $a$ and $b$, on a single line, separated by a space.
The judge will then respond with three values $c_a\ c_b\ s$. These are the card values at position $a$ and positions $b$ (Which will both be represented as a two character upper-case string from `A-Z`), as well as an integer $s$ which determines whether all cards are face-up or not (1 for yes, 0 for no).



### Constraints

* All card values will be represented as the concatenation of two upper-case strings from `A-Z`.
* All queries should satisfy $1 \leq a, b \leq 2N$
*  $1 \leq N \leq 80$
*  $1 \leq T \leq 100$

### Example Run

```
[JUDGE]      2
[JUDGE]      4
[SUBMISSION] 1 4
[JUDGE]      AB BC 0
[SUBMISSION] 1 6
[JUDGE]      AB AB 0
[SUBMISSION] 2 8
[JUDGE]      LF PO 0
[SUBMISSION] 2 3
[JUDGE]      LF LF 0
[SUBMISSION] 4 7
[JUDGE]      BC BC 0
[SUBMISSION] 5 8
[JUDGE]      PO PO 1
[JUDGE]      80
... (Continues to play second game with N=80)
```
