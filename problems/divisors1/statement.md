# Divisors [I]

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

For this first problem, we'd like to consider a collection of values from this sequence, and try to order them based on their apperance in the sequence.

For example, if given the values ~1_1, 2_4, 1_5, 5_1, 3_2, 2_3~ we would order these as ~1_1, 1_5, 5_1, 2_3, 3_2, 2_4~.

## Input

Input will begin with a single integer ~n~, representing the length of the following sequence.
The next line will contain ~n~ space separated values in the form `i_j`, representing the value ~i_j~ in the sequence.

## Output

Output a single line with ~n~ space separated values in the form of `i_j`, the sorted version of what was passed through in input.

## Constraints

* ~1 \leq n \leq 10^5~
* ~1 \leq i, j \leq 10^9~

## Example

#### Input
```
6
1_1 2_4 1_5 5_1 3_2 2_3
```

#### Output
```
1_1 1_5 5_1 2_3 3_2 2_4
```
