# Mirror Images

Kasey is a digital artist who designs 8 bit logos for her clients.
She is a bit of a lazy (a.k.a. inventive) worker though, and wants to get the most out of her designs.

Whenever Kasey makes a design to give to clients, she also tries flipping her art to give additional designs to other clients.
With just flipping alone, there are 4 axis against which Kasey can flip her square artwork, and generate 7 other designs:

TODO: Image

However, Kasey doesn't want to give two identical images to her clients, or they will suspect something. Can you help Kasey identify how many unique flip designs there are?

## Input

Input will start with a single integer $n$, the height/width of the design.
Input will then contain $n$ lines, each containing $n$ characters (either `.` or `X`)

## Output

Output should contain a single integer $k$, the number of unique designs possible

## Example

**Input**

```
4
X..X
.X..
..X.
X..X
```

**Output**

```
2
```

There are only two possible designs:

```
X..X
.X..
..X.
X..X
```

and

```
X..X
..X.
.X..
X..X
```

## Constraints

* $1 \leq n \leq 1000$
