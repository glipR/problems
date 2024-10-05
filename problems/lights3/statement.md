# Lights [III]

The blurb for this problem is the same as Lights [I], save for the statement of the problem.

You stand before an infinitely long corridor containing lights and their respective switches.
You'd like to turn a subset of the lights on using little robots that will flick certain switches infinitely along the corridor.

In this third problem, you'll be sending an infinite number of robots. The ~i^\text{th}~ robot will flick switches according the the following rule:

Robot ~i~ flicks light switch ~j~ if ~2i-1~ divides ~j~. In other words, the ~i^\text{th}~ robot flicks every ~(2i-1)^{\text{th}}~ switch.

A light switch stays on if after all robots are done, it has been flicked an odd number of times. For example, Light Switch ~#4~ is on because it was flicked by Robot 1. While Light Switch ~#3~ is off because it was flicked by Robots 1 and 2.

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
2
```
#### Explanation
3 is the only light switch that is turned off.

#### Input
```
6
```
#### Output
```
3
```
#### Explanation
1, 2, 4 are the only light switch that is turned on.

#### Input
```
10
```
#### Output
```
5
```
#### Explanation
1, 2, 4, 8, 9 are the only light switches that are turned on.
