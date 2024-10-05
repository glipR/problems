# Miscellaneous [III]

The Tales of Helga is a single player game which is played by the protagonist Chain.

The game is played on a 2d grid, in order to beat the game, Chain will need to collect all two pieces of the di-force and then only then can they defeat the final boss Nox

There's a recent trend going on called "Random Plays Helga", whereby this game is played with completely random inputs (random inputs being up, down, left, right). You are interested in the *expected* number of turns it takes "Random Plays Helga" to beat the game on a specific map.

(If an invalid input is entered, then the player just stands where they are).

## Input

Input will contain two integers ~n~ and ~m~ representing the height and width of the playable map.
The next ~n~ lines will contain strings of ~m~ characters, representing the map. The characters will be one of the following:

* `.`: Empty terrain - Chain can move here.
* `X`: Walled terrain - Chain cannot move here.
* `A` or `B`: One piece of the di-force - If Chain moves to this location, they collect the di-force piece.
* `S`: The spawn point for Chain.
* `G`: The final boss Nox - If chain moves to this location *after* collecting all pieces of the di-force, they win the game.

## Output

Output a single value representing the expected number of steps to beat the game. Your answer must have an absolute or relative difference of at most ~10^{-6}~

## Constraints

* ~1 \leq n \times m \leq 10^3~

## Example

#### Input

```
3 5
XXXBG
XXX.X
S.A.X
```

#### Output

```
84
```

1. The chances that we finish the game in 6 steps is ~\frac{1}{4^6}~
2. The chances that we finish the game in 7 steps is ~\frac{1}{4^6} \times \frac{1}{2} {5 \choose 1} + \frac{1}{4^6} \times \frac{3}{4}~ (Either our first move is a dud (3/4 chance) or one of the following 5 moves takes us nowhere (1/2 chance))
3. ~\cdots~

Continuing this process ad infinitum we get:

~~
\frac{6}{4^6} + 7 \times (\frac{1}{4^6} \times \frac{1}{2} {5 \choose 1} + \frac{1}{4^6} \times \frac{3}{4}) + \cdots = 84
~~
