\textit{\small Note that the statement is same as ``Hearty Forgger I'', except for constraints}

Alice is playing a variant of \textit{Frogger}.

This game is played on a $b \times b$ grid, indexed by (0, 0) from the bottom left, with the $x$ axis spanning left to right.
On the grid, there are a number of horizontal, possibly overlapping, single height trucks, of varying lengths, which contains \textit{hearts}.

\begin{center}
\includegraphics[bb=0 0 375 190]{GridPairing.PNG}
\end{center}

Every time-step, the trucks move 1 unit to the right, wrapping around the board from right to left. Simultaneously, the player will move one unit up the grid, until falling off the top of the grid, at which point the game is over.

Whenever the player is on top of a truck (including when the player spawns, at its starting row), the player earns the amount of hearts contained within the truck.

Therefore, the only input Alice has into the outcome of the game is the player's spawn, as well as the time at which this spawn occurs.

Alice has only a few options for such spawn locations and times, and she wants to maximize the amount of hearts gained before she finishes the game. Can you help her?

## Input

The first line contains 3 integers: $b, p, q$.

$p$ lines follow, denoting the locations of trucks on the map.
Each line contains 4 integers: $x_i, y_i, l_i, h_i$.

$x_i, y_i$ denotes the location of the left side of the truck, while $l_i$ denotes the length of the truck. $h_i$ denotes the total heart value of this truck.

After this, $q$ lines follow.
Each line contains 4 integers: $x_j, y_j, t1_j, t2_j$.

This denotes a singular spawn point, as well as a start and end time ($t1_j$ and $t2_j$ respectively, both inclusive) under which Alice can spawn here.


\Large{\textbf{Constraints}}

$1 \leq b \leq 10^5$.\\

$0 \leq p, q \leq 3b$\\

$0 \leq x_i, y_i, x_j, y_j < b$.\\

$0 \leq t_1 \leq t_2 \leq 10^8$\\

$0 < l_i \leq b$
$0 < h_i \leq 10^4$

## Output

$h$, the maximum number of hearts achievable from one spawn location at one time, given the above information.

```
5 4 2
3 2 3 2
3 3 2 1
1 3 1 5
0 4 3 3
3 0 0 0
1 1 5 6
```

Case 0 can achieve 6 hearts by beginning at (1, 1) at time 6.
