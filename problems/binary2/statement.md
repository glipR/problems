# Binary Sequences [II]

The blurb for this problem is the same as Binary Sequences [I], save for the statement of the problem.

This set of problems is centered around a sequence generated in the following manner:

1. Take all natural numbers in increasing order
2. Replace each natural number with its binary representation
3. Concatenate these into a single sequence

For example, the first 4 natural numbers generate the first 8 digits in the sequence: `11011100`.

The first digit is `1`, for `1`. The next two are `10`, for `2`. The next two are `11`, for `3`, and the final three are `100`, for `4`.

In this second problem, we want to find the number of `1`s that occur in the sequence at or before index ~i~. So if we kept a running total of the prefix sums of our sequence, we'd get:

```
12234555
```

as the first 8 digits.

## Input

Input will consist of a single natural number ~i~.

## Output

Output a single integer, representing the numbner of 1s in the sequence at or before (1-indexed) index ~i~.

## Constraints

* ~1 \leq i \leq 10^{18}~

## Examples

#### Input
```
3
```
#### Output
```
2
```

#### Input
```
4
```
#### Output
```
3
```

#### Input
```
8
```
#### Output
```
5
```
