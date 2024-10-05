# Block pathing

You are an ant on a childs toy, and would like to find the shortest path between two points.
The childs toy simply contains two objects: An axis-aligned rectangle and a circle.

You can assume that:

* The two objects don't overlap
* The two objects don't "kiss" (there is a non-zero distance between the two)

What is the shortest distance from start to finish?

## Input

Input will always have the same number of values, all of which are integers, in the following form:

```
sx sy
ex ey
blx bly trx try
rad cx cy
```

Where:

* `sx` and `sy` are the x/y coordinates of the starting position
* `ex` and `ey` are the x/y coordinates of the end goal
* `blx` and `bly` are the x/y coordinates of the bottom left corner of the rectangle
* `trx` and `try` are the x/y coordinates of the top right corner of the rectangle
* `rad` is the radius of the circle
* `cx` and `cy` are the x/y coordinates of the centre of the circle

## Output

Output a single value representing the shortest distance from the start to end goal. Any answer with absolute or relative error of $10^{-6}$ will be considered correct.

## Example

Take the following input:

```
1 1
14 14
2 2 7 7
4 11 11
```

This is represented by the following graph:

IMAGE

Which can be pathed in the following manner:

IMAGE

Resulting in a distance of

```
21.625015745078453
```

## Constraints

* All values given are in the range $[0, 10^9]$
