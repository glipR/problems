<img src="https://me.glipr.xyz/img/comp/cybercrime.png" alt="problem header" width="180"/>

The year is 30XX, and we have robots with binary DNA. Cyber-Crime is at an all time high, and DNA evidence is still the primary source for catching suspected criminals.

In this particular situation, you have a whole swab of binary DNA from a crime scene. This swab is cyclic, meaning that there is no start and end of the sequence.

You know the swab *contains* the robber's exact DNA string. You'd previously copied out the portion of DNA relating to the criminal. However, it turns out that the criminal had a very special kind of DNA, that mutates itself when copied!

In particular, every bit of DNA has a specific chance to flip, and you've been left with this mutated mess.

Given the large number of possible strings the DNA could have mutated from, you want to find the top 3 most likely DNA strings we started with (in particular, we want you to point them out on the long cycle of DNA).

### Input

Input will being with two integers, $N$, the length of the binary DNA cycle, and $M$, the length of the mutated substring.

The next line will contain $N$ bits, space separated. This represents the binary DNA cycle.

The next line will contain $M$ bits, space separated. This represents the mutated mess.

The next line will contain $M$ numbers, $p_i$, space separated. $p_i$ is the probability that the $i^{th}$ bit was flipped in the mutation process.

### Output

Print 3 1-indexed positions $a, b, c$ that represent the 3 most likely starting positions for the mutated mess.
If 1 or 2 positions are only possible, then only print those positions. All tests cases will have at least one valid position.

For each position $x$, we can denote $d_x$ to be the probability that if the DNA was copied from position $x$, that the mutation would yield what we have in the input.

Your output will be considered correct if all 3 positions $a$, $b$, $c$ have $d_a, d_b, d_c$ within relative error $e^{10^{-3}}-1 \approx 10^{-3}$ of the correct 1st, 2nd and 3rd responses respectively. If you respond with an impossible position, or less positions than are possible (For example responding with 2 positions when 3 are possible) you will get WA.

### Constraints

* $1 \leq N \leq 10^6$
* $1 \leq M \leq N$
* $p_i = 0$, $p_i = 1$, or $0.1 \leq p_i \leq 0.9$

### Example Run

Input
```
11 8
0 1 1 0 1 1 1 0 1 0 0
0 0 1 1 1 1 1 0
0.2 0.8 0 0 1 0.5 0.5 0.5
```

Output
```
4 11
```

Explanation

Because of the string of 1 1 1 with flip probability 0, 0 and 1, there are only two possible places this could go: positions 2, 3, 4 or positions 6, 7, 8. This corresponds to the mutated strings starting at positions 11 and 4 respectively.
We have $d_{11} = 20\%$ and $d_4 = 80\%$.
