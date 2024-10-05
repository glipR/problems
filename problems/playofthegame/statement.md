<img src="https://me.glipr.xyz/img/comp/playofthegame.png" alt="problem header" width="180"/>

Following the extreme success of "Kicking Kangaroo", you've decided to begin developing the world's first "First Pouch-son Shooter" - A game where Kangaroos play soccer and kick to shoot goals (We've already got a team name in mind).
As part of this game, at the end of any match a "play of the game" replay is selected to highlight the skills of one particular player.
Given that the game is relatively simple, your game can calculate what peak performance is within any particular game, as a string of inputs. So you'd like to award the play of the game to whichever player can start off this string of inputs and hold it for as long as possible.
Input will give the inputs of each player over the course of the game, as well as the inputs considered "peak performance". You should award the play of the game to the player who has the longest contiguous subsequence of frame data which is identical to a prefix of the frame data for the "peak performance" input. "Longest" is measured in number of frames, not inputs, and inputs between frames can be placed in any order, and still be considered equivalent.

## Input
Input will begin with 2 space separated integers, the total number of players `p` and the maximum length of a player input string `s`.
After this `p` lines follow, each containing a single string of length at most `s` characters, comprising of only character set `wsad|`
These are the inputs for players `1` to `p` in order.
After this a single line follows, containing 2 space separated strings. The first is at most 4 characters long, comprising of only character set `wsad-` , and the second at most `s` characters long, comprising of only character set `wsad|`. This is the starting state of the "peak performance" and frame data respectively.
The inputs should be interpreted as follows:

* `wsad` represents a toggling of the input for buttons `wsad` respectively.
* `|` represents the start of a new frame.
* `-` only ever appears as a lone character, and simply means that no buttons are pressed at the beginning of peak performance.
* It is assumed that for all players, they begin with no buttons pressed, however for the play of the game, the play must start with the buttons pressed which were provided in the first string of the last line of input.

A contiguous subsequence of frame data matches `x` frames of play if:

* The contiguous subsequence starts either at the beginning of input or directly after a | symbol AND:
* In the previous frame (or beginning of input, depending on above) the pressed buttons matches the starting state of "peak performance"
* For the first `x` frames of peak performance input, the pressed buttons at the end of every frame exactly matches the pressed buttons of the player input for the same frame, provided frame 0 was the start of the contiguous subsequence.

## Output

If there is no point in time at which the starting state of the play of the game is even reached, print `No Play of the Game`.
Otherwise, find the contiguous subsequence of frame data matching the largest number of frames of play, and print the player number, number of frames matched, and starting frame in the following format: `Player #1 matched 3 frames starting at frame #2.`

* You don't have to deal with correct plural grammar and such for frames. 0 frames is fine, as is 1 frames.
* There is an assumed "final frame" which is captured after all input in both the player input and "peak performance" input. So for a "peak performance" input containing `x` many `|` characters, a sequence of inputs can actually match `x+1` frames.

## Constraints

* $1 \leq p \leq 10^4$.
* $1 \leq s \leq 10^6$.
* The total length of all player input will not exceed $10^6$.

## Example Run
For input

```
2 15
as|s|sda|ds|sw
s|das|ds|s|as
as s|das|ds|s
```

Your program should output:

```
Player #1 matched 3 frames starting at frame #2.
```

Notice that even though Player #2 repeats the entire string of inputs that is "peak performance", it does not do so with the correct starting configuration of buttons (as). However, it does match a single frame at the end, since s|das|ds results in button configuration `as`