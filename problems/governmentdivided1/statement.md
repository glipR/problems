You are founding a new government MGD (Monash Government of Delegation), and the first order of business is to get ~N~ units of work done.
However, just like a good government official, you wish to delegate ~100%~ of this work.

The only rule you must follow is that each subordinate must receive an equal amount of work, and that this work is kept in integer portions.

You are interested in how many distinct ways you could achieve this.

## Input / Output

Input will begin with an integer ~1 \leq T \leq 10^5~, the number of test cases. ~T~ lines follow.
On each of these lines is a single integer ~1 \leq N \leq 2*10^6~, the number of units of work to be done.

You should output ~T~ lines - the possible ways to delegate ~N~ units of work, for each respective ~N~.

## Example

Input

```
2
6
16
```

Output

```
4
5
```

For case ~N=6~, we can give 1 subordinate 6 units of work, 3 subordinates 2 units of work, 6 subordinates 1 unit of work, or 2 subordinates 3 units of work.

For case ~N=16~, we can give 1 subordinate 8 units of work, 2 subordinates 4 units of work, 16 subordinates 1 unit of work, 8 subordinates 2 units of work, or 4 subordinates 2 units of work.
