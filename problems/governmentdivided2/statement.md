You are founding a new government MGD (Monash Government of Delegation), and the first order of business is to get ~N~ units of work done.
However, just like a good government official, you wish to delegate ~100%~ of this work.

But, the people you are delegating to are also politicians, and so they will also delegate ~100%~ of their work.

This pattern continues for ~k~ steps. Again, the only presiding rule is that if someone delegates work to a group of people, every person has to receive the same integer amount of work.

Additionally, no person can receive delegated work from two individuals, so this delegation forms a tree, rooted at yourself, where every leaf is distance ~k~ away from you.

You are interested in counting how many distinct trees you can make with this form of delegation. Two trees are considered distinct if there is no isomorphism between the two, *keeping the root where it is*.

## Input / Output

Input will contain a single line, containing two integers ~1 \leq N \leq 10^{12}~, the number of units of work to be done, and ~1 \leq k \leq 10~, the levels of delegation that occur.

You should output a single integer - the number of possible ways to delegate ~N~ units of work, for each respective ~N~.

Since this number can be quite large, output the number modulo 1000000007

*IMPORTANT RESTRICTION*:

For any pair ~N, k~ you are given, you know that the number of distinct trees with parameters ~N, k-1~ is ~\leq 10000~. Note the ~k-1~!!

## Example

Input

```
6 2
```

Output

```
12
```

There are 12 distinct trees with ~k = 2, N = 6~. Two examples of divisions are:

![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/gov_div1.png)
