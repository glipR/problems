Your friend is an avid rock collector, and you want to play a prank on him.

Your friend stores all of their rocks on a circular, rotating cupboard. This cupboard has three levels, and $n$ positions around the perimeter. In each of the $n$ positions, a rock can be on the top level, middle level, and the bottom level. At first, the 1st position points true north.

All of the rocks are distinct, but to your friend, they are indistinguishable. You wish to rotate the table, so that they cannot tell it has changed. They could tell the table has changed if the position of the rocks seems to have changed. For example, if the lower level position pointing true north did have a rock originally, it should still have a rock after rotation.

### Input

Input will begin with a single integer, $T$, the number of test cases.  $T$ lines follow.

Each test case will begin with a single integer, $N$, the number of positions on a single level of the table.
Then 3 lines follow. Each line begins with a single integer, $k_i$, the number of rocks on that particular level. That line then contains $k_i$ integers, specifying the positions of these rocks (in order from $1$ to $N$).
### Output

For each test case, output a single integer $x$, the number of possible rotations you could make to prank your friend.

### Constraints

* $1 \leq T \leq 1000$
* $1 \leq N \leq 10^{18}$
* $0 \leq k_i \leq 10^6$
* The sum of $k_i$ over all test cases does not exceed $10^6$

### Example Run

Input
```
2
6
2 2 5
2 3 6
4 1 2 4 5
12
6 3 4 7 8 11 12
6 2 4 6 8 10 12
0
```

Output
```
1
2
```

Explanation

See image below for rotations for test cases 1 and 2.
