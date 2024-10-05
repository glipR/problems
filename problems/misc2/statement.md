# Miscellaneous [II]

Treetown is a town of various suburbs connected by main roads. The roads have been constructed in such a way that:

* Every suburb can be reached by taking these roads from suburb to suburb
* Between any two suburbs, there is only a single path connecting the two
* All roads are bidirectional

The nature of this construction means that a single road failure leads to a disconnection of the town, causing major delays. You'd like to analyse the possible impact of removing a road from Treetown.

Every road in Treetown has a distance ~d_j~. For any pair of suburbs ~a, b~ in Treetown, we compute the contribution to the Treetown economy as

~~
\sum_{i \in R} d_i
~~

Where ~R~ is the collection of roads on the path from ~a~ to ~b~. For example, take the following graph, with 4 suburbs, ~a, b, c, d~ and 3 roads from ~a~ to ~b~, ~b~ to ~c~ and ~c~ to ~d~, of lengths 1, 3 and 4.

Then for the suburb pairing ~a~ and ~c~, the contribution to productivity is

~~
1 + 3 = 4,
~~
summing the roads from ~a~ to ~b~ and ~b~ to ~c~.

In this problem, we want you to assess the reduction in productivity after removing a single road (in other words, summing the productivity contribution of suburb pairings that are connected via the removed road.)

For example, removing the edge ~b~ to ~c~ would remove pairings ~ac~, ~ad~, ~bc~, ~bd~, which contribute ~4 + 8 + 3 + 7 = 22~ productivity.

## Input

Input will begin with a single integer ~N~, representing the number of suburbs.
~N-1~ lines will follow. Each line will contain 3 space separated integers, ~i~ ~j~ and ~d~. This means there is a road from ~i~ to ~j~ of distance ~d~.

Finally, a single integer ~x~ will follow. This represents a (1-indexed) index of one of the roads just inputted.

## Output

Output should contain a single integer - the hit to productivity removing road ~x~ would cause.

## Constraints

* ~1 \leq N \leq 2\times 10^5~
* ~1 \leq d \leq 10^3~

## Example

#### Input
Taking the example in the statement, this can be written as:
```
4
1 2 1
2 3 3
3 4 4
2
```

#### Output
For which the output should be
```
22
```
as discussed previously.
