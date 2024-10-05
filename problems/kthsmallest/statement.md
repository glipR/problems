This problem is *interactive*, which means you need to communicate with the grader using standard input and output.

You have a series of $q$ non-decreasing sequences of positive integers, each of length $k$. You'd like to find the $k^{th}$ smallest value of all of these sequences collectively.

For example, suppose $q = 4$ and $k = 5$, with the following sequences:

```
[19, 32, 51, 239, 258]
[31, 349, 380, 6736, 6767]
[24, 24, 709, 18506, 18530]
[2, 27, 29, 60, 62]
```

The 1st smallest value is 2, the 2nd smallest value is 19, the 3rd and 4th smallest value is 24, and the 5th smallest value is 27.
So the answer to this particular problem would be 27, at the 4th queue in the 2nd position.

But, for this problem, you don't know the entirety of every sequence. You can only make 3000 queries to figure out a particular value, after which you need to guess the $k^{th}$ smallest value.

## Interaction

Interaction will begin with the judge printing 3 space-separated integers $q$, $k$ and $m$; The number of queues, the value of $k$, and the maximum value of any of the queues.

After this, you are free to start querying. There are two types of queries you can make:

1. `VAL q i`: Judge will print the value for queue `q` and index `i` (In the example above, `VAL 4 2` prints `27`)
2. `ANS q i`: Submit your answer to the judge. If successful, test is passed. If unsuccessful, then the test fails.

For both queries, both `q` and `i` must be valid or the judge will fail you. For `ANS` queries in the case of duplicate $k^{th}$ smallest values, any one will do.

## Constraints

**Test Set A - 20%**

* `N_QUERIES = 3000`
* $1 \leq q \leq 5$
* $1 \leq k \leq 300$
* $1 \leq m \leq 10^{10}$

**Test Set B - 20%**

* `N_QUERIES = 3000`
* $1 \leq q \leq 10$
* $1 \leq k \leq 500$
* $1 \leq m \leq 10^{10}$

**Test Set C - 20%**

* `N_QUERIES = 3000`
* $1 \leq q \leq 10$
* $1 \leq k \leq 5000$
* $1 \leq m \leq 10^{15}$

**Test Set D - 40%**

* `N_QUERIES = 3000`
* $1 \leq q \leq 100$
* $1 \leq k \leq 20000$
* $1 \leq m \leq 10^{40}$
