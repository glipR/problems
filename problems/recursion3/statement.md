# Recursion [III]

We introduce a new recursive sequence, which satisfies:

~~
\begin{cases}
    H(0) = 0 &  \\
    H(n) = 4\times H(n-1) + \sum_{n-1}^{i=1} ((n-i)^2\times F(i-1)) & n \geq 1
\end{cases}
~~

Where ~F(n)~ is the nth fibonacci number, following the previous definition.

For example, ~H(0), H(1), H(2), H(3), H(4)~ can be written as ~0, 0, 1, 9, 51~

In this question, you must compute ~H(n)~ for some value ~n~. Since the value may be quite large, output your answer modulo ~10^9+7~.

## Input

Input will contain a single integer ~n~

## Output

Output should contain a single integer, representing ~H(n) \text{mod} 10^9+7~.

## Constraints

* ~0 \leq n \leq 10^18~

## Example

#### Input
```
5
```
#### Output
```
240
```
