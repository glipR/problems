# Divisors [0]

Let's consider the string of all natural numbers: ~1, 2, 3, 4, \ldots~

We'd like to find the sum of the first ~n~ values of this sequence, although that alone is a bit boring (how would we do this?)

Instead, we'd like to find the sum, only after doing a simple operation to the individual sequence values - taking their value modulo some ~m~.

For example, for ~n=5~, ~m=4~, the sequence of the first 5 elements would be: ~1, 2, 3, 0, 1~, and the total sum would be 7.

## Input

Input will contain two space-separated integers ~n~ and ~m~, mirroring the definition from the statement

## Output

Output a single integer representing the sum of the first ~n~ elements modulo ~m~.

## Constraints

* ~1 \leq n \leq 10^9~
* ~1 \leq m \leq 10^9~

## Example

#### Input
```
5 4
```

#### Output
```
7
```
