# Stick Man

StickMan is played on a rectangular grid which wraps around itself (exiting left of the screen returns you on the right side of the screen), just like Pacman.

The aim of the game is to get to the endzone quickly, while picking up coins to increase your score. However, the squares on the grid are sticky, and slow you down for a specific amount of time.

In order to win this particular game of stickman, you want to get to the end zone as fast as possible, and within these constraints, you'd also like to maximise the number of coins you pickup.

What is the path which is the shortest to get to the endzone, and among these shortest path, which one maximises the number of coins picked up?

## Input

Input will begin with two numbers, $n$ and $m$, the height and width of the playing field respectively.
Next follows $n$ lines representing the field. Each line will contain $m$ space-separated values, which will either be:

* Some positive integer $d$, representing the stickiness of this cell
* `W`, representing an impassable wall
* `S`, representing the spawn point (with stickiness 0)
* `G`, representing the end goal (with stickiness 0)

Another $n$ lines then following containing a string of length $m$, representing the positions of coins.
Cells with coins are represented by `*`, while cells without coins are represented by `X`

The time taken on a path through the grid is simply the sum of the stickiness values of the cells in this path

## Output

Output a list of directions (`U D L R` representing Up, Down, Left or Right) that minimise distances, and within these constrains maximises coins.

## Constraints

* 1 \leq n*m \leq 10^6
* All stickiness values are at most 1000

## Example

**Example Input**

```
5 4
1 2 W W
10 1 W G
W W W W
W 4 1 S
3 5 4 W
*XXX
*XX*
XXXX
X**X
*XXX
```

**Example Output**

```
LLDDLDL
```

**Explanation**

This path steps on cells with stickiness values 1,4,5,2,1,10, so the total time taken is 23 units, which is minimal. This path also picks up 5/6 coins, which is the most that can be collected in 23 units of time.
