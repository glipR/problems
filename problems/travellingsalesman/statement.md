A rather famous problem in computer science is the travelling salesman problem (TSP).

In this problem we have a salesman, who moves between different cities, selling their wares.
The salesman wants to visit every city exactly once, and end up where he began.

Your friend Jordan thinks they've got a solution! And he just needs you to write a program to check that his output actually gives a valid cycle for the salesman (A cycle that meets every city exactly once).

For a collection of ~n~ cities, Jordan's program outputs a collection of ~n~ movements, from one city to the next. So we should be able to reconstruct the cycle by joining all of these movements together.

For example, a cycle that starts at city 1, goes to city 3, then city 4, then city 2 and finally returns to city 1 would be represented as: `1 3`, followed by `3 4`, `4 2` and `2 1`. The order of these pairs matters, and so does the order of the individual numbers within the pairs (`1 3` is different from `3 1`).

## Input

Input will start with a single integer ~T~, the number of test cases.

For each test case, input begins with a single integer ~n~, the number of cities. ~n~ lines follow, containing two integers ~a_i~ and ~b_i~. This represents a movement from city ~a_i~ to city ~b_i~.

## Output

For each test case, if the movements represent a valid cycle for the salesman, print `GOOD`.

If the movements do not represent a valid cycle, then print `BAD`.

## Constraints

~1 \leq T \leq 100~
~2 \leq n \leq 30~
~1 \leq a_i, b_i \leq n~

## Example run

Input
```
3
4
4 2
2 1
1 3
3 4
7
1 2
2 3
3 1
1 4
4 5
5 6
6 1
4
1 2
3 2
3 4
1 4
```

Output
```
GOOD
BAD
BAD
```

Explanation
* Case 1 is ok, as it represents the cycle 4-2-1-3-4.
* Case 2 is not ok, while it is a cycle, we visit 1 twice, and do not visit 7.
* Case 3 is not ok, 1-2-3-4-1 is a cycle, but the order of movements `3 2` and `1 4` is wrong, they should be `2 3` and `4 1`.
