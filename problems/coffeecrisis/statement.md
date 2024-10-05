<img src="https://me.glipr.xyz/img/comp/coffeecrisis.png" alt="problem header" width="180"/>

Julie is studying a bachelor of computer science, and is gearing up for an insanely long semester with hellish workloads.

Her plan of attack for the coming twelve weeks is a frenzy of caffeine consumption, and luckily she knows just the barrista to help. Kyle is a special barrista, who only sells a single, special, coffee each day.
Kyle's coffee has three characteristics:

* Duration: How long the effects of the coffee last, in days.
* Strength: How many assignments the coffee will allow you to complete in a day.
* Caffeine Content: How much caffeine is in the drink, in tens of mg.


On days where Kyle isn't feeling too creative, he'll offer the standard coffee, which has 1 Duration, 1 Strength, and 1 Caffeine Content.
To avoid over-dependence and eventually numbing the effects of the coffee, Julie has imposed the following rules:

* She cannot drink one coffee while still receiving the effects of another coffee
* If a coffee has $x$ Caffeine Content, she will not drink another coffee for $x$ days.


Within these bounds, deciding which coffee to drink on which days is stumping Julie, since she hasn't finished her algorithms unit yet. Can you help her complete as many assignments as possible?

## Input
Input will begin with two integers, $D$, the number of days in the semester, and $N$, the number of special coffees that Kyle will offer throughout the semester.
Input will follow with $N$ lines, containing 4 space separated integers:

* $T_i$: the day on which coffee is sold (Days are indexed from 1)
* $D_i$: the duration of the coffee.
* $S_i$: the strength of the coffee.
* $C_i$: the caffeine content.

## Output
Output should begin with a single integers, $A$, the number of assignments Julie can complete. The next line should contain $N$ characters, each character `a_i` is either a `*` or `-`, representing whether Julie purchased the `i`th special coffee from input (Assume that Julie purchased the standard coffees where possible)

## Constraints

* $1 \leq D \leq 10^9$
* $1 \leq N \leq 10^5$
* $1 \leq T_i \leq D$
* $1 \leq D_i \leq 10^9$
* $1 \leq S_i \leq 10^3$
* $1 \leq C_i \leq 10^9$
* All $T_i$ will be unique

## Example Run
For input
```
30 4
6 12 20 14
19 12 10 100
13 8 20 30
3 10 20 4
```
One possible output is:
```
362
--**
```
Julie can complete 2+20x10+20x8 assignments buy drinking the standard coffee for 2 days, the special coffee on day 3, the special coffee on day 13. She cannot instead drink the special coffees on days 6 and 19, because there is too much caffeine in coffee 6. For a similar reason, she cannot drink the standard coffee from days 21-30.