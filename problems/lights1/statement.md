# Lights [I]

You stand before an infinitely long corridor containing lights and their respective switches.
You'd like to turn a subset of the lights on using little robots that will flick certain switches infinitely along the corridor.

In this first problem, you'll be sending an infinite number of robots. The ~i^\text{th}~ robot will flick switches according the the following rule:

Robot ~i~ flicks light switch ~j~ if ~i~ divides ~j~. In other words, the ~i^\text{th}~ robot flicks every ~i^\text{th}~ switch.

A light switch stays on if after all robots are done, it has been flicked an odd number of times. For example, Light Switch ~#4~ is on because it was flicked by Robots 1, 2 and 4. While Light Switch ~#5~ is off because it was flicked by Robots 1 and 5.

## Input

Input will contain a single integer ~n~, representing how many lights we'll be considering

## Output

Output will contain a single integer, representing the total number of lights at position at or before the ~n^\text{th}~ light that are on at the end of execution

## Constraints

* ~1 \leq n \leq 10^{18}~

## Examples

#### Input
```
3
```
#### Output
```
1
```
#### Explanation
1 is the only light switch turned on

#### Input
```
4
```
#### Output
```
2
```
#### Explanation
1 and 4 are the only light switches turned on
