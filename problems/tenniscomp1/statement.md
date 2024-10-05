Alexandra is running a tennis tournament between friends to determine who is the best, but Alexandra thinks she knows the general skill level of everyone in the competition.
As such, she wants to predict the outcome of every game in the tournament, but she needs your help to simulate the tournament and predict results.

The tournament is a single elimination bracket, where a single loss removes you from the bracket, and a win brings you to the next stage, with half the competitors. This continues until only one team is remaining.
One famous example of single elimination brackets are the [tennis grand slams](https://ausopen.com/draws).

Alexandra gives every competitor a skill level, and predicts that the higher skill level competitor always wins. (If there is a draw, she predicts the lexicographically smallest competitor wins, due to [Alphabetism](https://studyfinds.org/success-last-name/))

Can you print all games that Alexandra thinks will occur, as well as Alexandra's expected outcome?

## Input

Input will start with a single integer $c$, the number of competitors in the tournament. This will always be a power of 2.

Next follows $c$ lines, each containing a string, followed by an integer.
This is the name of the competitor and the skill level of that competitor.

The way battles will be selected is based on the order of the names specified in input. For example, if the input to the problem has

```
4
name1 4
name2 7
name3 2
name4 10
```

Then the first 2 battles will be name1 vs name2, and name3 vs name4.
The same ordering is then used for subsequent battles - the winner of name1 vs name2 plays the winner of name3 vs name4, and the winner of name5 vs name6 plays the winner of name7 vs name8, and so on.

## Output

Output should begin with a single integer $p$, the number of games.

## Constraints

* $2 \leq c \leq 1024$.
* $c$ is always a power of 2.
* Each name contains only lowercase english letters and numbers.
* Each name is at most 20 characters long.
* Each skill level $s$ satisfies $1 \leq s \leq 10^9$.

## Example Test Case

For input:
```
4
name1 4
name2 7
name3 2
name4 10
```

The program should output:

```
3
name2 defeats name1
name4 defeats name3
name4 defeats name2
```
