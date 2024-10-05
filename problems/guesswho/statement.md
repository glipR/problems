Harriet is playing popular game "Guess Who?", in which she has to try guess a particular character based on their features, out of a list of characters.
In this game Harriet can make queries about this character, to reduce the possible choices.

## Interaction

This is an interactive problem, meaning you read and write your solution simultaneously.

Input will start with two integers, ~n~ and ~f~, separate by a space.
~f~ lines follow, listing the features each character has. A feature is a single string containing only upper/lower case letters.
~n~ lines follow, describing ~n~ different characters. Each line contains ~f~ space separate strings - the values for each characteristic (Each value is also a string containing only upper/lower case letters).

From here, interaction begins. You can make two possible queries:

* `QUERY A = B`: Ask whether the character has value `B` for feature `A`. The judge will respond either `YES` or `NO`.
* `GUESS x`: Guess that the character is index `x` (1 indexed). After making this query, your code should exit.

## Limits

* You can make at most 20 queries (including `GUESS`)
* ~1 \leq f \leq 6~
* ~1 \leq n \leq 1000~
* Each feature has at most 4 possible values that can appear

## Example Interaction

```
### JUDGE:
4 3
Hair
Eyes
Hat
Brown Blue Cap
Blonde Blue Beanie
Blonde Green None
Grey Brown Beanie
### SOLUTION:
QUERY Eyes = Blue
### JUDGE:
NO
### SOLUTION:
QUERY Hair = Beanie
### JUDGE:
YES
### SOLUTION:
GUESS 4
```

In this example, the fourth character (With Grey Hair, Brown Eyes, and a Beanie for the Hat) is the character we are trying to guess.
