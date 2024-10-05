<img src="https://me.glipr.xyz/img/comp/screechingbirds.png" alt="problem header" width="180"/>

Every morning you wake to the soothing sounds of squawking and screeching magpies, cockatoos, and crows.
Over the years you have named everyone of the birds, as well as the noise they make. Additionally, you've also notice that all these birds make sounds in a pattern.
Every bird repeats the same sound every $x$ seconds, where each bird can have it's own value of $x$.
This morning, you'd like to try calculate what sounds you'll first hear on waking up.

### Input

Input will begin with two space-separated integers, $B$ and $S$. $B$ is the number of birds that will make sounds, and you'll need to calculate the first $S$ sounds that you hear.
$B$ lines will follow, each containing two integers and a string, $f_i$, $p_i$ and $s_i$, all separated by a space. These three values represent:

1. The time the bird first makes a sound ($f_i$)
2. The number of seconds the bird will wait before repeating the sound ($p_i$)
3. The sound the bird makes ($s_i$)

### Output

Output $S$ lines, the first $S$ sounds made in the morning, given that time starts at $0$.
If two birds make a sound at the same time, assume the bird given earlier in input makes the sound first.
Constraints

* $1 \leq B \leq 50$
* $1 \leq S \leq 500$
* $0 \leq f_i \leq 100$
* $1 \leq p_i \leq 100$
* $s_i$ will only contain lowercase alphabet characters, and length will not exceed 25 characters.

### Example Run
For input

```
3 7
2 5 squaw
0 3 breepip
5 2 keeki
```

Your code should produce output

```
breepip
squaw
breepip
keeki
breepip
squaw
keeki
```

### Explanation

At time 0, a breepip is heard. After this, at time 2, a squaw is heard. After this, at time 3, a second breepip is heard, then at time 5, a keeki is heard. At time 6, a third breepip is heard. Then at time 7, a squaw and keeki is heard, but the squaw bird appears before the keeki bird in input, so it's sound is heard first.