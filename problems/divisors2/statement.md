# Divisors [II]

The blurb for this problem is the same as Divisors [I], save for the statement of the problem.

Consider the sequence of all natural numbers, and then for each number, listing each of the divisors of this number in increasing order:

~~
    1 2 3 4 5 6 \ldots
~~

becomes:

~~
    1 1 2 1 3 1 2 4 1 5 1 2 3 6 \ldots
~~

Since this (infinite) sequence has a lot of duplicates, we can notate for each digit whether it is the first, second, third... occurence using a subscript:

~~
    1_1 1_2 2_1 1_3 3_1 1_4 2_2 4_1 1_5 5_1 1_6 2_3 3_2 6_1 \ldots
~~

For the second problem, we'd like to find the exact index of a particular value. For example, ~1_1~ has index 1, ~1_2~ has index 2, ~2_1~ has index 3, and so on.

## Input

Input will contain a single value `i_j`, representing value ~i_j~

## Output

Output a single integer representing the 1 index of the value in the sequence

## Constraints

* ~1 \leq i \times j \leq 10^{11}~

## Example

#### Input
```
5_1
```

#### Output
```
10
```
