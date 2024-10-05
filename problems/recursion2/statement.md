# Recursion [II]

We introduce a new recursive sequence, which satisfies:

~~
\begin{cases}
    G(0) = 0 &  \\
    G(1) = 5 &  \\
    G(n) = 2\times G(n-1) + 3\times G(n-2) + F(n-1) & n \geq 2
\end{cases}
~~

Where ~F(n)~ is the nth fibonacci number, following the previous definition.

For example, ~G(0), G(1), G(2), G(3), G(4)~ can be written as ~0, 5, 11, 39, 114~

In this question, you must compute ~G(n)~ for some value ~n~. Since the value may be quite large, output your answer modulo ~10^9+7~.

## Input

Input will contain a single integer ~n~

## Output

Output should contain a single integer, representing ~G(n) \text{mod} 10^9+7~.

## Constraints

* ~0 \leq n \leq 10^18~

## Example

#### Input
```
5
```
#### Output
```
350
```
