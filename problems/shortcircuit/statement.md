<img src="https://me.glipr.xyz/img/comp/shortcircuit.png" alt="problem header" width="180"/>

Jane is an electrician, and has had a mess of an electronic circuit sent her way.
The circuit is a rectangular grid of metal cubes, and each cube has it's own "resistance factor".
This resistance factor determines how much voltage is needed for electricity to flow through this cube (voltage is not consumed in the process, this is simply a threshold that needs to be met). For example to pass through a cubes with resistance factor 4, 9, 6, 2 the electricity needs to have voltage at least maX(4, 9, 6, 2) = 9.

Attached to some of the cubes are positive terminals and negative terminals. Jane has a dial, which she can use to change the voltage of electricity coming out of each negative terminals.

Jane wants to know the minimum voltage she can set the dial to, so that each positive terminal has electricity reached through one of the negative terminals.

## Input

Input will begin with two space-separated integers, `w` and `h`, the width and height of the rectangular grid.
`h` lines follow, each containing `w` characters from the set `.NP`, representing empty, negative and positive terminals respectively.
`h` lines follow, each containing `w` space separated integers, representing the resistance factor $r_{xy}$ of the corresponding cube.

## Output

Output should contain a single integer `q`, the lowest required voltage to connect all positive terminals to some (not necessarily the same) negative terminal.

## Constraints

* There will always be at least one positive and at least one negative terminal in the grid.
* $2 \leq w \times h \leq 3 \times 10^4$
* $0 \leq r_{xy} \leq 10^9$

## Example Run

For input

```
5 4
..NP.
P....
.P...
..N..
17 14 7 20 100
13 21 100 100 100
100 12 9 100 100
100 100 10 5 1
```

The answer is 20, since each positive terminal is connected to a negative terminal when electricity has voltage 20 as follows:

```
xxNP.
P....
.Px..
..N..
```

Where an `x` represents cubes that electricty is passing through (and all N and P blocks also have electricity passing through them)
