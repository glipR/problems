<img src="https://blog.monashicpc.com/new_binder/assets/img/comp_assets/scuttle_bug.jpg" alt="georgia the scuttlebug" width="300"/>

Georgia (above) is a Scuttlebug hosting her own Scuttlebug Jamboree!

To host a Scuttlebug Jamboree, she needs to collect a berry for each Scuttlebug attending.
However, these berries Georgia needs are on the other side of a river. 

In order to collect some integer ~b~ amount of berries, Georgia needs to make ~b~ round trips, starting on the south side of the river, jumping to the north side of the river, and then coming back to the south side of the river.

Georgia can travel from one side of the river to the other by jumping on lily pads. Lily pads however, don't float well, and so after Georgia jumps on a lily pad, it sinks, meaning Georgia cannot use the lily pad again. 

Viewing the area as a 2d plane, with the ~y~ axis pointing north/south and the ~x~ axis pointing east/west, the south side of the river sits at ~y=0~ and extends east/west indefinitely, and the north side of the river sits at ~y=h~ and extends east/west indefinitely.

Georgia wants to know the largest distance she has to jump to collect her berries and get the Jamboree started!

## Input

The first line of input contains 3 integers, ~h~, ~n~ and ~b~, separated by a space.

~h~ represents the y-position of the north side of the river (~2 \leq h \leq 10^7~).

~n~ represents the total number of lily pads in the river (~0 \leq n \leq 300~).

~b~ represents the total number of berries that Georgia needs to collect (~1 \leq b \leq 100~).

Then follows ~n~ lines, each containing two integers ~x_i, y_i~, the location of the ~i^{\text{th}}~ lily pad (~-10^7 \leq x_i \leq 10^7~ and ~0 < y_i < h~).

## Output

The largest (euclidean) distance Georgia has to jump can be always expressed as ~\sqrt{d}~ for some integer ~d~. 

Output should begin with two integers: ~d~ and ~l~. ~l~ is the length of Georgia's path that collects ~b~ berries.

After this ~l~ lines should follow, each line containing a location in Georgia's path. If the location is a lily pad, print the integer coordinates of the lilypad. If the location is the north or south side of the river, output `N` or `S` accordingly.

## Other

For the purposes of this problem assume that lily pads have 0 width, so the distance jumped between two lily pads is simply the difference between their coordinates.

Georgia can also jump from one side of the river to the other.

## Example Run

Input
```
4 4 1
0 1
-1 3
1 3
3 2
```

Output
```
5 7
S
0 1
-1 3
N
1 3
3 2
S
```

Explanation

With `d = 5`, Georgia can jump from the south side to `0 1`, then `-1 3`, to the north side and collect a berry, and then jump from the north side to `1 3`, `3 2` and finally back at the south side. Since she now has `b` berries, so she can host her scuttlebug jamboree!

![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/scuttle_example.png)
