# Binary Sequences [I]

This set of problems is centered around a sequence generated in the following manner:

1. Take all natural numbers in increasing order
2. Replace each natural number with its binary representation
3. Concatenate these into a single sequence

For example, the first 4 natural numbers generate the first 8 digits in the sequence: `11011100`.

The first digit is `1`, for `1`. The next two are `10`, for `2`. The next two are `11`, for `3`, and the final three are `100`, for `4`.

In this first problem, we just want to find the value of the "ith" value in the sequence. So the answer for `1` would be 1, for `2` would be `1`, for `3` would be `0`, and so on. The bitstring above is the answers for the inputs `1` through to `8`.

## Input

Input will consist of a single natural number ~i~.

## Output

Output a single 0 or 1, representing the value of the sequence at (1-indexed) index ~i~.

## Constraints

* ~1 \leq i \leq 10^{18}~

## Examples

#### Input
```
3
```
#### Output
```
0
```

#### Input
```
4
```
#### Output
```
1
```

#### Input
```
8
```
#### Output
```
0
```
