# Banana 1

## Problem Statement

Jackson is head ranger at the zoo, which looks after many manic monkeys.

Every day, Jackson needs to buy enough bananas to placate the monkeys, so they do not start a monkey uprising.

Jackson can only buy bananas in packs of ~10~. How much money must Jackson spend?

## Input

Your first line of input will contain two space-separated integers, ~n~ and ~c~: the number of monkeys and the dollar cost for ~10~ bananas, respectively.

Next, ~n~ lines will follow, each containing a single integer ~a_i~: the number of bananas needed to placate monkey ~i~.

## Output

A single line, containing the total cost of bananas Jackson has to buy, in dollars.

## Constraints

For all test cases...
* ~1 \leq n \leq 10^6~
* ~1 \leq c \leq 10^2~
* ~1 \leq a_i \leq 10^5~

## Example 

### Input
```
4 6
15
8
31
42
```

### Output
```
60
```

### Explanation

Jackson needs to buy at least ~15+8+31+42=96~ bananas. 

Jackson will have to buy at least ~10~ packs of ~10~ bananas (a grand total of ~10 \times 10 = 100~ bananas) to satisfy the need for ~96~ banana. 

Since each pack of bananas costs ~10~ dollars, this will cost Jackson a total of ~6 \times 10 = 60~ dollars.

## Python Template
```python
n, c = map(int, input().split())
a = [int(input()) for _ in range(n)]
# Continue your code here and print your final answer!
```