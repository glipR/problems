Erin is working on a science experiment showing the process of fungus infection and decay.

She has made a tree structure of ecosystems, which are favourable for the fungus. In particular:

* The fungus spawns at node 1
* The fungus decays after ~x~ days
* Each edge in the tree represents a pathway by which the fungus can expand it's network.
* Each edge has a transmissibility factor ~t_i~, If a fungus is on one side of the edge, after ~t_i~ days it will appear on the other side.
* If a fungus decays at a particular node, then fungus cannot reappear there.

So over time, the fungus moves down the tree, decaying at earlier nodes as this happens. Eventually, all nodes will decay, and the reaction will be over.

Erin is particularly interested in the communication that seems to go between components of alive fungus:

* Each day, every fungus node ~i~ that is connected to another fungus node ~j~ via fungus nodes sends information to each other.
* This information expends ~d(i, j)^2~ joules of energy - The square distance in the tree between ~i~ and ~j~.

To ensure that the reaction doesn't take too long, Erin's tree is constructed such that the fungus will only ever move through at most 6 nodes in a path from start to finish (The fungus can infect much more than 6 nodes, but the longest path from start to finish will be length 5)

So at the start of each day the following happens (in this order):

* For existing fungus nodes, energy is expended.
* If for edge ~i~, ~t_i~ days have now passed since the fungus has reached an adjacent node, then a new fungus appears on the other side of the edge. (Regardless of whether the original fungus still exists).
* If a fungus has been alive for ~x~ days, then it decays.

Erin is interested in how much energy is expended over the entire experiment.
Since this number can be rather large, output the result modulo ~10^9+7~

## Input

Input will start with a single integer ~T~, the number of test cases.
For each test case, input will start with 2 integers ~x~ and ~n~. ~x~ is the number of days it takes for a fungus to decay, and ~n~ is the total number of nodes in the tree.

Then, ~n-1~ lines will follow, containing 3 integers, ~a~, ~b~ and ~t_i~. ~a~ and ~b~ are adjacent nodes in the tree, and ~t_i~ is the transmissibility of the edge.

## Output

You should output ~T~ lines, on each line, output a single integer, the answer to the specific test case.

## Constraints

* ~1 \leq T \leq 10^3~
* ~1 \leq n \leq 2 \times 10^5~
* The sum of ~n~ over all test cases will not exceed ~2 \times 10^5~
* ~1 \leq t_i \leq 10^9~
* ~1 \leq a, b \leq n~
* ~1 \leq x \leq 10^9~
* The graphs in tests will always describe a tree such that ~d(1, i) \leq 5~ for all ~i~.

## Example Run

Input
```
2
3 6
1 2 1
1 3 1
2 4 2
2 5 1
3 6 4
4 5
1 2 1
2 3 2
3 4 2
4 5 1
```

Output
```
32
18
```

The fungus moves down the tree in the following manner, with arrows representing work done (see diagram):

![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/fungus1.png)
![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/fungus2.png)

So the answer in the first test is 0+6+20+6+0+0+0 = 32, and the answer in the second test is 0+1+1+6+1+1+6+1+1=18.
