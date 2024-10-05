# Coins [III]

In this problem you are presenting with ~n~ evenly weighted coins, except you aren't! ***Three*** of the coins are actually heavier than the others (and are equally heavy), and you want to find them efficiently.

You are equipped with a *three-sided* seesaw, meaning you can put three piles of coins on the 3 sides and observe what piles are heavier than others.

In this interactive problem, determine the weighted coins using the seesaw, making few queries.

## Interaction

This is an interactive problem. So rather than reading input once and printing output once, your program should communicate to the judge using input and output.

Interaction will start with a single integer ~n~, the number of coins. These coins are labelled 1 through to ~n~ inclusive.

Queries may then start. Your program can use the seesaw by writing a query of the form

```
TEST {pile 1} | {pile 2} | {pile 3}
```

Where pile 1/2/3 are space separated integers. For example, to weigh coins 1 and 3 against coins 2 and 4 against coins 5 and 6, you can do:

```
TEST 1 3 | 2 4 | 5 6
```

The judge will then print `1`, `2` and `3` separated by `>` to indicate piles are bigger than each other. For example: `1 2 > 3` would mean that while piles 1 and 2 weigh the same, both are heavier than pile 3. Whereas `3 > 1 > 2` means that pile 3 is heavier than pile 1 which is in turn heavier than pile 2.

Once you've determined the weighted coins, you end interaction by printing `ANS {coin1} {coin2} {coin3}`. For example `ANS 3 6 5`.

## Constraints

* ~3 \leq n \leq 10^5~
* The total number of queries should not exceed 27.

## Example interaction

```
[JUDGE]:    8
[PROCESS]:  TEST 1 2 | 3 4 | 5
[JUDGE]:    2 > 1 > 3
[PROCESS]:  TEST 4 | 3 |
[JUDGE]:    1 > 2 > 3
[PROCESS]:  TEST 7 8 | 5 6 | 1 3
[JUDGE]:    2 1 > 3
[PROCESS]:  TEST 5 7 | 1 3 | 6 8
[JUDGE]:    3 > 1 2
[PROCESS]:  ANS 4 6 8
```
