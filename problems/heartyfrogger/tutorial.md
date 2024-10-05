In order to solve this problem, we need to first leverage the fact that each truck moves in the same direction at the same speed.

As such, all paths through the grid from particular spawn points are left diagonal lines, starting on the same row as the spawn point.

\begin{center}
\includegraphics[bb=0 0 425 190]{Diagonal.PNG}
\end{center}

As such, if we reorganise the board by shifting each row by 1 step further to the right, as we move up the board, our previously left diagonal lines become straight ones.

As a truck movement to the right is equivalent to the spawn point moving to the left (Frame of reference, as the board is cyclic on the horizontal), to account for spawn times, we only need to shift ourselves along the starting row to the left.

\begin{center}
\includegraphics[bb=0 0 475 190]{Shifting.PNG}
\end{center}

Because a $b\times b$ or $b\times (p+q)$ solution is infeasible, we need to smartly evaluate the highest score from each spawn point, using previous computation.

One such way is to use a list of size $b$, with some optimized operations. Notice that we must do strictly \textbf{more} computation to evaluate the heart value of spawn points lower down on the board, so let's sweep through the board from top to bottom, and try to gleam some information.

Let our list $l$ store the following values, as we pass by row $x$:

$l_y$ = Hearts redeemed at point $(y, x)$ (In the transformed space), assuming we spawn at time 0.

\begin{center}
\includegraphics[bb=0 0 475 190]{segtree.PNG}
\end{center}

Notice that in transitioning $l$ from row $x$ to row $x-1$, we only need to add the trucks on row $x-1$. Therefore as we pass by row $x$, we do the following:

\begin{itemize}
    \item Add the information of all trucks in row $x$ to our list
    \item For all spawn points in row $x$, calculate their best heart value from $l$.
\end{itemize}

Now, if we used a plain old array to do this, our complexity would be $(p+q)\times b$. But, because all updates and queries to the list are in fact range based queries, we can use a segment tree to satisfy this list, and reduce time complexity to $(p+q)\log(b)$.
