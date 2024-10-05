<img src="https://me.glipr.xyz/img/comp/funrace.png" alt="problem header" width="300" style="display: block; margin: auto"/>

Giancarlo is organising this year's annual go-kart race. This race is purely for fun, and so he wants to maximise the excitement that the race can generate.
A race with more racers is always more fun, however, the skill level of each racer is not equal, and we don't want the race to be a blowout.

Each racer has a skill level, and its up to Giancarlo to decide what racers to pick so that he maximises the number of racers while avoiding a blowout.

A race is a *blowout* if the racers can be broken up into two sets, so that all racers in one set are at least 5 skill levels below everyone in the other set. For example, the race with skill levels [9, 13, 3] is a blowout with sets [3] and [9, 13], however the race with skill levels [9, 13, 3, 6] is not a blowout.

Can you help Giancarlo?

## Input

Input will begin with a single integer $n$, the number of available racers.

The next line contain $n$ space-separated integers $s_i$, the skill levels of the available racers.

## Output

Output should contain three integers:

* The total number of racers Giancarlo can include in the race
* The smallest skill level of a racer in the race.
* The highest skill level of a racer in the race.

## Constraints

* $1 \leq n \leq 10^6$
* $1 \leq s_i \leq 10^9$

## Example Run

For the following input

```
7
22 9 25 13 3 19 14
```

Your program could output

```
3 19 25
```

or 

```
3 9 14
```

Since two valid maximal choices are racers `[22, 25, 19]` or `[9, 13, 14]`.
