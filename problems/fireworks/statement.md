Giuseppe is lighting fireworks to celebrate the completion of his Code Quest bot.
Unlucky for him, his neighbours will kill him if he lights fireworks in his backyard, so he will just stick to imaginary fireworks for now :)

In Giuseppe's 2D world, fireworks explode at some point in space, then rain down glitter in a cone until they hit the floor.
For example, if Giuseppe lit some fireworks at the coordinates (3, 3), (8, 4) and (10, 2) on a board of size 12 * 7, the picture would start like this:

```
............
............
........x...
...x........
..........x.
............
............
```

With (0, 0) being the bottom-left cell, and the first coordinate specifying horizontal direction while the second coordinate specifying the vertical direction.
After letting the fireworks explode, they would fall to the ground and make the following pattern:

```
............
............
........x...
...x...+++..
..+++.++++x.
.+++++++++++
++++++++++++
```

Can you help Giuseppe imagine the fireworks of his dreams and print the resulting pattern?

## Input

Input will begin with three integers $n$, $m$ and $f$, representing the width and height of the board, as well as the number of fireworks.
$f$ lines follow, each containing two integers $x_i, y_i$. This tells us the location of the $f_i^{\text{th}}$ firework

## Output

Output an n*m board of `.x+` representing the firework explosion. An `x` should always be shown where a firework exploded - it shouldn't be overwritten by `+`s.

## Constraints

Test Set A

* $1 \leq n, m \leq 10^2$
* $1 \leq f \leq 20$

Test Set B

* $1 \leq n, m \leq 10^3$
* $0 \leq f \leq 10^4$

Solving all of Test Set A will net you 50% of the score for this problem.

## Example Test Case

Input:
```
12 7 3
3 3
8 4
10 2
```

Output:
```
............
............
........x...
...x...+++..
..+++.++++x.
.+++++++++++
++++++++++++
```
