Connecting the many states of IEEEtopia is a series of train lines, that form a [tree](https://en.wikipedia.org/wiki/Tree_(graph_theory)) structure, with states forming nodes, and train lines forming edges.

Each train line is paired with a luxury restaurant, for the ultimate culinary experience on your trip. Each restaurant sells a single item, for $d_i$ dollars.

The citizens of IEEEtopia are rather stingy; for any trip between two states, they will always purchase the *cheapest* meal along the unique path between these two states.

Assuming that one citizen tries all possible pairings of states and moves between them (order does not matter here, $1 \to 2$ is equivalent to  $2 \to 1$ and should not be double counted), how much money will be spent?. Since this answer may be quite large, output the answer modulo  $10^9+7$.

### Input

Input will contain a single integer $N$, the size of the tree.

 $N - 1$ lines follow, each containing three integers,  $a$, $b$ and $c$, signifying a train line between states $a$ and $b$, with a restaurant cost of $c$. (States are numbered $1$ to $N$).

### Output

Output a single integer, the total money spent modulo $10^9+7$.

### Constraints

* $1 \leq N \leq 10^6$ 
* $1 \leq a, b \leq N$ 
* The edges specified will definitely denote a tree.
* $0 \leq c \leq 10^9$

### Example Run

Input
```
5
1 2 1
1 3 2
2 4 3
2 5 4
```

Output
```
18
```

Explanation

We write $a \to b: c$ to mean that the trip from  $a$ to $b$ costs $c$.

 $1\to 2: 1$, $1\to 3: 2$, $1\to 4: 1$, $1\to 5: 1$, $2\to 3: 1$, $2\to 4: 3$, $2\to 5: 4$, $3\to 4: 1$, $3\to 5: 1$, $4\to 5: 3$.

 This sums to 18 total.
