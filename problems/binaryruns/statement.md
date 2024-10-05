Rachel is playing a game of Binary Runs.

In this game, you generate a binary string, and the aim is to get the longest run: The longest contiguous substring of the same value. So the longest run in 0111000011 has length 4: 0000.

Rachel starts with an empty string, and has the following options:

* Add a new digit to her current string, which is equally likely to be 0 or 1.
* Flip the last digit of her current string.

At the moment the game can go on forever, and Rachel can keep flipping digits until she is pleased. To make it more interesting, and to limit the length of the game, the following rules are introduced (Assume that anything higher than ~100%~ definitely happens):

* If Rachel flips a digit, there is a ~(0.1 \times x)%~ chance that a new digit is added to her current string instead, where ~x~ is the length of her current run (So the longest suffix of her string with all the same values). 
* If Rachel adds a new digit to her current string, there is a ~(0.03 \times x)%~ chance that the last digit of her string gets flipped instead, using the same definition for ~x~.
* On every action Rachel makes, there is a ~0.01%~ chance that the game ends before the action is made, and her current binary string is her final string.

None of these rules apply on the first action (Which will always be add a new digit).

Rachel will always play the following way:

* If the last two digits in her string are not equal, she will try to flip the last digit.
* Otherwise (and when she does not have two digits in her string), she will add a new digit.

Rachel wants to know, given some binary string ~b~, the chances that she will at some point have this as her current string.

## Input

Input will consist of one line: The binary string ~b~ Rachel is considering. The length of this binary string will be at most ~10^5~ and at least 1.

## Output

The probability that Rachel will at some point have this binary string ~b~ as her current string is expressible as some irreducible fraction ~\frac{p}{q}~.
Output ~pq^{-1}~ mod ~1000000007~, where ~q^{-1}~ is the modular inverse of ~q~ mod ~1000000007~.

## Example

Input
```
0
```

Output
```
71407146
```

This is because Rachel can have 0 as the current string in two ways:

* She gets 0 as the first digit (~\frac{1}{2}~ chance)
* She gets 1 as the first digit, then tries to add, but the bit gets flipped instead (~\frac{1}{2} \times \frac{9999}{10000} \times \frac{3}{10000}~ chance)

So in total, we have a ~\frac{100029997}{200000000}~ chance of seeing 0, and we find:

```
(71407146 * 200000000) % 1000000007 = 100029997
```
