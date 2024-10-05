Jakob is head ranger at the zoo, which looks after many manic monkeys.

Every day, Jakob needs to buy enough bananas to placate the monkeys, so they do not start a monkey uprising.

Jakob has a few vendors to choose from, which all sell him different amounts of bananas for different costs. He can buy from each vendor as much as he wants, and can also buy excess bananas if need be.

What is the minimum amount of money Jakob must spend to placate the monkeys?

### Input

Input will begin with a two integers, $N$ and $M$, the number of monkeys, and number of vendors.

Next, $N$ lines follow, each containing a single integer $a_i$, the number of bananas needed to placate monkey $i$.

Next, $M$ lines follow, each containing two integers $a_j$ and $c_j$, the amount of bananas and cost for each vendor. (You can buy $a_j$ bananas for $c_j$.)

### Output

Output the minimum cost for Jakob.

### Constraints

* $1 \leq N \leq 10^3$
* $1 \leq M \leq 30$
* $1 \leq a_i \leq 10^2$
* $1 \leq a_j \leq 10^6$
* $1 \leq c_j \leq 10^8$

### Example Run

Input
```
4 3
15
8
31
42
1 1000
2 10
5 20
```

Output
```
390
```

Explanation

In total we need to buy at least 15+8+31+42=96 bananas. We can achieve this by buying 95 bananas from the 3rd vendor, for 380, then 2 bananas from the second vendor, for 10.
