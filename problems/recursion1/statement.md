# Recursion [I]

The Fibonacci Sequence is a famous sequence defined by the recurrence relation:

~~
\begin{cases}
    F(n) = 1 & 0 \leq n \leq 1 \\
    F(n) = F(n-1) + F(n-2) & n \geq 2
\end{cases}
~~

For example, ~F(0), F(1), F(2), F(3), F(4)~ can be written as ~1, 1, 2, 3, 5~

In this question, you must compute ~F(n)~ for some value ~n~. Since the value may be quite large, output your answer modulo ~10^9+7~.

## Input

Input will contain a single integer ~n~

## Output

Output should contain a single integer, representing ~F(n) \text{mod} 10^9+7~.

## Constraints

* ~0 \leq n \leq 10^18~

## Example

#### Input
```
5
```
#### Output
```
8
```
