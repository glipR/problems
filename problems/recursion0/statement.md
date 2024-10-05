# Recursion [0]

In this problem we'll be evaluating the recursive function ~G~, where ~G(0)=0~, ~G(1)=1~, and for anything larger:

~~
G(n) = 3\times G(n-1) + G(n-2)
~~

For example, ~G(2) = 3~, ~G(3) = 10~, ~G(4) = 33~, and so on.

Since the number computed may be large, you should compute the value modulo ~10^9+7~

## Input

Input will contain a single integer ~n~.

## Output

Output should be a single integer, ~G(n) \% 10^9+7~.

## Constraints

* ~0 \leq n \leq 10^6~
