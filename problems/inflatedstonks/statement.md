<img src="https://me.glipr.xyz/img/comp/stonks.png" alt="problem header" width="180"/>

You are the CEO of Diamonds Galore, the new up-and-coming mining company that has a special drilling technique guaranteed to get diamonds.
Gathering funding for these machines is however a very expensive and length process. As such you'd like to pump up the market value of your company by repeatedly recording great mining trips with the single drill you currently own.

Your current mining territory is represent by an `n` by `n` grid, with each grid square having an integer value, representing the amount of diamonds in this grid square. Whenever you place the drill in one location, it will mine all of the diamonds in that location.
Your mining territory is also sloped, meaning that after mining in one location, you can only move in one cardinal direction to continue mining.

A mining day occurs as follows:
* You start mining at a particular location.
* You keep mining at a location, moving to the next grid square, and so on until:
    - You move off of the grid
    - You hit a grid square which you've already mined at (either today or a previous day)
* The stock price for your company increases by `Number of Diamonds Mined * Number of Grid Squares Diamonds were mined from`.

You are interested in the largest you can pump the stock price by, given that you can spend as many days as possible mining.

## Input
Input will begin with a single integer `n`, the size of the grid world.
`n` lines follow, each containing `n` characters from the set `ULDR`, this represents whether the slope of the grid square will push the mining drill Up, Left, Down or Right.
`n` lines follow, each containing `n` space separated integers `d_{xy}`. This represents the number of diamonds within a particular grid square.

## Output
After deciding on your mining trips, start by outputting a single integer `t`, the number of trips.
After which, you should print `t` lines, each containing a single `y` and `x` index, this is the location you will begin mining at on each day, in order. (`x` is the horizonal index, starting at 0 and growing to the right. `y` is the vertical index, starting at 0 and growing downwards.)

## Constraints

* $1 \leq n \leq 10^2$
* $0 \leq d_{xy} \leq 10^6$
* The maximum possible length of a mining trip on your grid will not exceed $4n$.

## Example Run

For the following input
```
4
RRDL
LUDR
UULL
RRLL
4 8 2 10
1 1 1 1
1 1 1 1
6 1 1 4
```

Your program could output
```
7
3 0
3 3
0 3
0 0
2 3
2 0
1 3
```
* On day #1, the drill will visit (3, 0), (3, 1), (3, 2), mining 6+1+1=8 Diamonds in 3 locations, for a bump of 24 in stock price.
* On day #2, the drill will visit (3, 3), mining 4 Diamonds in 1 location, for a bump of 4 in stock price.
* On day #3, the drill will visit (0, 3), (0, 2), (1, 2), (2, 2), (2, 1), (1, 1), (0, 1), mining 24 Diamonds in 7 locations, for a bump of 168 in stock price.
* On day #4, the drill will visit (0, 0), mining 4 Diamonds in 1 location, for a bump of 4 in stock price.
* On day #5, the drill will visit (2, 3), mining 1 Diamond in 1 location, for a bump of 1 in stock price.
* On day #6, the drill will visit (2, 0), (1, 0), mining 2 Diamonds in 2 locations, for a bump of 4 in stock price.
* On day #7, the drill will visit (1, 3), mining 1 Diamond in 1 location, for a bump of 1 in stock price.

In total this amounts to 24 + 4 + 168 + 4 + 1 + 4 + 1 = 206 stock price, the best possible.
