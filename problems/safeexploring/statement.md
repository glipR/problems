Tanya supervises a parkland area famous for its hiking and scenic walks.
This parkland is divided into ~n \times m~ sections in a grid, that is ~n~ units long and ~m~ units wide.

For each of these sections, Tanya has recieved an altitude reading. From these values, Tanya can calculate the steepness of neighbouring sections. For two neighbouring sections, with altitudes ~a~ and ~b~, their steepness is calculated as

$$
    | a - b |,
$$

as you might expect. Each section is neighbour to 4 other sections, in the cardinal directions (Excluding the edges of the grid).

Tanya knows that currently there are some hikers in the area, who all have different abilities when it comes to hiking through steep territory, and she wants to know how many grid squares they can safely reach.

## Input

Input will begin with 3 integers ~n, m, q~. ~q~ is the number of hikers.

After this ~n~ lines will be printed, each containing ~m~ integers. These integers denote the altitude of the associated grid square.

After this, ~q~ lines will be printed.

Each of these lines contain 3 integers, ~a, b~ and ~s~. ~a~ is the x-coordinate of the hiker , ~b~ is the y-coordinate of the hiker, and ~s~ is the largest steepness they can safely traverse.

Coordinates are 1-indexed. With respect to the input, ~x~ coordinate goes from left to right, and ~y~ coordinate goes from top to bottom

## Output

Output should contain ~q~ integers on separate lines: The total number of grid squares that the hikers can reach (Including the one they are currently on).

## Constraints

* ~1 \leq n, m \leq 500~
* ~1 \leq q \leq 10^5~
* ~0 \leq s \leq 300~
* ~1 \leq a \leq m~, ~1 \leq b \leq n~

## Sample Run

Input
```
3 2 3
1 4
3 6
2 1
1 1 2
2 1 2
2 3 1
```

Output
```
4
2
3
```

Explanation:

* In test case one, the hiker begins at the top left of the grid. From here they can move down, down again, and then to the right, to cover 4 squares.
* In test case two, the hiker begins at the top right of the grid. From here they can only move down, to cover 2 squares.
* In test case three, the hiker begins at the bottom right of the grid. From here they can only move left, and then up, to cover 3 squares.
