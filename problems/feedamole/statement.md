### Statement

You are the zookeeper for a very hungry set of moles, which live underground. When it's time to feed, these moles sporadically pop their heads out of various holes to receive sustenance in the form of various grubs.

To keep the moles happy, you'd like to feed as many grubs as possible to the various moles, luckily since you know the moles so well, you also know when each mole likes to pop up and what holes it tends to pop up from. Can you figure out the most grubs fed within the time limit?

The Mole Enclosure is a `W * H` square metre grid containing a mole-hole in each square metre of land. For example, an enclosure with `W = 4`, `H = 2` would look like this:

```
X X X X
X X X X
```

Where an `X` represents a mole-hole.

Your grub hand can only be hovering over a singular mole-hole at the end of any second of feeding time, and if you do have your hand over the mole-hole when a mole is poking it's head out you can feed it a grub. In the span of a second, you can move your grub hand orthogonally through the enclosure 1-metre.

So in the example above, if a mole was feeding at the top-left hole at the 1st second of feeding time, and a mole was feeding at the bottom-left hole at the 2nd second of feeding time, you could feed both moles by starting your grub hand at the top-left hole for the 1st second, and in-between the 1st and 2nd second moving your hand 1 metre down to the bottom-left hole.

### Input / Output

Input will begin with 3 space-separated integers:

- The width of the mole enclosure, in metres, `W`
- The height of the enclosure, in metres, `H`
- The total length in seconds of feeding time for the moles, `T`

Input will then contain T lines, each containing multiple space separated integers representing a particular second of feeding. The first integer on each line will be a single integer `M`, representing the total number of moles peeking out of holes at the current second. The line will then contain an additional `2*M` integers, where a pair `X`, `Y` represents the position of a mole currently peeking out (`X` represents the column number, 1 being left and `W` being right, while `Y` represents the row number, 1 being top while `H` being bottom).

Output should being with a single integer - the number of grubs you can feed to the moles in the time specified. `T` lines should follow, each containing 2 space separated integers, representing the position of the grub hand for each respective second of feeding.

### Bounds

**Test Set 1:**

- ~1 \leq W, H \leq 3~
- ~1 \leq T \leq 5~

**Test Set 2:**

- ~1 \leq W, H \leq 40~
- ~1 \leq T \leq 100~

### Example Case

For the following input:

```
3 2 5
0
1 1 1
1 1 2
2 3 1 3 2
1 3 1
```

Possible output could be:

```
3
1 1
1 1
2 1
3 1
3 1
```

The mole states for each second are (With O representing a mole peeking):

```
X X X t = 1
X X X
-----
O X X t = 2
X X X
-----
X X X t = 3
O X X
-----
X X O t = 4
X X O
-----
X X O t = 5
X X X
```

And this can be solved by starting on the top-left for 2 seconds, then moving to the top-right and staying there for the last 2 seconds.
