A fancy new train has opened up in town, and the debut trip is today!

Many are interested in riding the train, but you are particularly interested in the hipsters who will ride the train.
If a hipster rides the train, they will write a positive article about the train, increasing the train's popularity.

However, hipsters are very picky about when they will board the train, they don't want to be seen as too mainstream.

In particular:

* At each station ~i~, we have ~h_i~ hipsters. 
* Before anyone boards, a train car is added to the back of the train with capacity for ~c_i~ passengers, to support increased demand for the train.
* Next, ~x_i~ passengers leave the train (If there are less than ~x_i~ passengers, then everyone leaves the train).
* If you allow them, each of the ~h_i~ hipsters will board the train only if the capacity of the train does not exceed ~y_i%~.
* At the same time that any hipster boards, ~z_i~ groupies will follow the hipster, increasing the capacity of the train. If these groupies would exceed the capacity of the train, the hipster cannot board.

Since so many people are eager to try the train out, you find yourself in control of who does / does not get to ride the train, in order to maximise the number of hipsters that board the train over the course of its journey.

## Input

The first line of input contains 2 integers ~s~ and ~c~, the number of stations and the initial capacity of the train (~1 \leq s \leq 1000~, ~0 \leq c \leq 10^9~).

~s~ lines follow, each containing 5 space-separated integers ~c_i, h_i, x_i, y_i, z_i~.

~0 \leq c_i \leq 10^9~ is the capacity of the attached train carriage.

~0 \leq h_i \leq 10000~ is the number of hipsters at the train station.

~0 \leq x_i \leq 10^9, 0 \leq y_i \leq 100, 0 \leq z_i \leq 10^9~ correspond to ~x_i, y_i, z_i~ in the problem statement.

**The sum of all ~h_i~ across all stations will not exceed ~10000~.**

## Output

You should print ~s~ integers, the number of hipsters you allow to board at each station.

## Example

Input
```
2 3
1 3 2 50 1
4 4 1 50 0
```

Output
```
1 4
```

For the first station, we can have:
* 0 hipsters board (0/4 capacity)
* 1 hipster board (2/4 capacity)
* 2 hipsters board (4/4 capacity) (Possible since 2/4 does not *exceed* ~50%~)

Once at the second station, 1 passenger leaves, and we have an 8 capacity train.
* If 0 hipsters boarded at station 1, we can have all 4 hipsters board for 4/8 capacity.
* If 1 hipster boarded at station 1, we can have all 4 hipsters board for 5/8 capacity.
* If 2 hipsters boarded at station 1, we can only board 2 hipsters for 5/8 capacity.

So the best option is to board 1 hipster at station 1, then all 4 at station 2, for a total of 5 hipsters.
