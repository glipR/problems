Jessica and Arjun are playing a Marble Swapping Game.

In this game, there are 2 types of high-tech marbles:

* Normal (Can be Red/Blue/Yellow/Purple/Green/Orange)
* Wild

Jessica and Arjun both begin with 7 marbles, and each player gets exactly 1 wild marble (as part of the 7). Players then take turns.

On any players turn, they pick one of their marbles, and one of the other player's Marbles. You cannot pick your own Wild marble.

If you pick the other player's wild marble, then all of your marbles (except your Wild Marble and your marble you picked) change colour.

In particular, Red becomes Blue, Blue becomes Yellow, ... and Orange becomes Red (You move one step along the list of colours at the beginning of the statement, wrapping around at the end).

Otherwise, if you picked one of the other players Normal Marbles, then your marble that you picked changes colour to the opposite of the colour that you picked in your opponents collection. The opposites of Red/Blue/Yellow/Purple/Green/Orange are Green/Orange/Purple/Yellow/Red/Blue respectively.

The aim of the game is to end up with one Marble of each colour, in addition to your Wild Marble.

Assuming Both Jessica and Arjun play optimally, you want to know if the game will end, and if so, who wins.

## Input

Input will begin with 1 integer ~T~, the number of test cases.

For each test case, 3 lines follow.
* The first is a string ~s~, which is either `Jessica` or `Arjun`. This denotes who plays first.
* The next is 7 space separated characters - Jessica's current marbles, which are represented as the first character of that particular colour, or `W` for wild. For example `R W Y P G P P` would mean Jessica has one Red marble, one Wild marble, One Yellow marble, one Green marble, and three Purple marbles.
* The next is 7 space separated characters in the same format - Arjun's current marbles.

## Output

Output should be ~T~ lines long.

For each test case output a single string:

* `Jessica` if Jessica wins
* `Arjun` if Arjun wins
* `Stalemate` if the game will continue indefinitely

## Constraints

* ~1 \leq T \leq 10^5~
* For each test case, both Jessica and Arjun will have exactly one Wild marble.
* For each test case, neither Jessica nor Arjun will begin with one of every colour.

## Example Input

Input
```
3
Arjun 
W R B Y P G G
W R R B Y P G
Arjun
R O B B Y W P 
R W R R O O O
Jessica
W B B O R B B
O P G G G W P
```

Output
```
Arjun
Jessica
Stalemate
```

Explanation:
In the first example, Arjun can pick one of his red marble, and the wild marble, to change the colour of the rest of his marbles.
In the second example, no matter what Arjun does, Jessica can turn one of her Red Marbles into a Green marble by selecting one of Arjun's Red marbles.

Arjun's turn in case 1:

![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/marble1.png)

Jessica's turn in case 2:

![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/marble2.png)