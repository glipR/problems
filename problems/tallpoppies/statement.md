# Tall Poppies

Will is a Florist who owns a flower bed of poppies.
Every day, all of Will's poppies will grow exactly $x$ centimetres taller.

As part of managing a healthy flower bed, Will does one of two things:

* Harvest the tallest poppy to sell at his shop
* Plant a poppy of height $y$ cm

Will would like to know the height of the poppies that he harvests so that he can set the correct selling price. Can you help him?

### Input

Input will start with three space-separated integers $x$, $P$ and $E$, the number of centimetres a poppy grows in a day, the number of poppies in the flower bed at day 0, and the number of events we'll be observing.
The next line will contain $P$ space-separated integers, the heights of the poppies at start of day 0.

$E$ lines will follow. Each of these $E$ lines will start with two space-separated integers, $d$ and $b$.
$d$ is the day on which this event is occuring (You may assume all events are occuring at the start of the day).

* If $b$ is 0, then this event is Will harvesting the tallest poppy in his flowerbed, and no more input will follow on this line.
* If $b$ is 1, then this event is Will planting a poppy, an additional integer will follow $p$, the height of this individual poppy.

**Example Input**

```
1 4 5
5 8 3 6
1 0
1 1 8
2 1 6
4 0
5 0
```

Here poppies grow at 1cm a day, and Will:

* Has 4 poppies to begin with at day 0, of heights 5, 8, 3 and 6 cm.
* On Day 1 - Will harvests the tallest poppy then plants a poppy of height 8cm
* On Day 2 - Will plants a poppy of height 8cm
* On Day 4 - Will harvests the tallest poppy
* On Day 5 - Will harvests the tallest poppy

### Output

If your input contains $X$ event lines containing $b=0$.
For each corresponding harvest event, you should print a single integer representing the height of the harvested poppy.

**Example Output**

```
9
11
11
```

* The poppies start off with heights 5, 8, 3, 6.
* At the start of Day 1, we have heights 6, 9, 4, 7 - so Will harvests the 9 height poppy.
* We plant an addition poppy, so new heights are 6, 4, 7, 8
* At the start of Day 2, we have heights 7, 5, 8, 9, and we plant a poppy of height 6
* At the start of Day 4, we have heights 9, 7, 10, 11, 7, and so we harvest the poppy of height 11
* At the start of Day 5, we have heights 10, 8, 11, 8, and so we harvest the poppy of height 11

### Constraints

* $0 \leq d \leq 10^9$ (Day of an event)
* $0 \leq p \leq 10^9$ (Individual poppy heights)
* $0 \leq x \leq 10$ (Growth per day)
* Harvest events will never occur when the flower bed is empty

**Test Set A** (50%)

* $1 \leq P \leq 100$ (Number of initial poppies)
* $1 \leq E \leq 100$ (Number of events)

**Test Set B** (50%)

* $1 \leq P \leq 10^6$ (Number of initial poppies)
* $1 \leq E \leq 10^6$ (Number of events)
