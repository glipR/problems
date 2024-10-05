You are in charge of 7 knights, which are guarding the castle from 7 trolls.

Every day, one of the trolls will either fall asleep or wake up.
On any given day, the knights know what trolls are asleep or awake, but they cannot communicate with one another. As such, they want to define a roster, which tells which knights to patrol based purely on whether the trolls are awake or asleep.

Because the knights don't want to grow tired, but also want to see each other, they want a roster that fits the following scheme:

* Each knight should patrol for at most $25\%$ of all possible sleeping states
* In at least $12.5\%$ of all possible sleeping states, all knights should be patrolling simultaneously
* Each possible sleeping state should have at least one knight on patrol
* If some sleeping state has a certain roster of knights, any 1-bit changes to the sleeping state should result in a different roster of knights (this can have some overlap of the knights however).

Can you come up with a scheme that fits all of the requirements?

### Input

No input is given.

### Output

Output should contain $2^7$ lines, describing the roster.
Each line should contain two binary strings, separated by a space. The first binary string should describe the sleeping state of the trolls (0 being asleep and 1 being awake), and the second binary string should describe whether a particular knight is patrolling (1 for patrolling, 0 for not).

### Example

If instead we had 3 knights (with percentage restrictions $50\%$ and $25\%$ respectively), the following might be a reasonable output:

```
000 111
100 100
010 010
110 001
001 001
101 111
011 100
111 010
```

* Every knight patrols at most $4/8 = 50\%$ of possible situations
* There are at least $2/8 = 25\%$ of possible situations where all knights patrol (`000` and `101`)
* Every state has at least one knight on patrol
* For any troll sleeping state, flipping a single bit results in a different roster. (For example, `010` has `010`, but flipping to `011`, `000` or `110` results in `100`, `111` and `001` respectively).