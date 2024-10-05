Harry is building a pasta bridge for an engineering competition.
Harry wants to try using many different types of right angled triangles, built up from three pasta noodles.

Harry already has two noodles picked out, with lengths ~a~ and ~b~. He wants to know if it is possible to cut a new length of noodle ~c~, such that the three pasta noodles can be combined together to create a right angled triangle.

## Input

Input will start with a single integer ~T~, the number of test cases.
~T~ lines follow. On each line, there will be two integers ~a~, and ~b~.

## Output
For each test case, output a single integer ~c~. 

If there is an integer length of noodle that can form a right angled triangle, ~c~ is the length of that noodle.
Otherwise, ~c~ is -1.

## Constraints

* ~1 \leq T \leq 10000~
* ~1 \leq a, b \leq 100000~

## Example Run

Input:

```
2
3 5
5 1
```

Output:

```
4
-1
```

Explanation:

If we have noodles of size 3, 5 and 4, we can create a right angled triangle as follows:

![](https://blog.monashicpc.com/new_binder/assets/img/comp_assets/triangle1.png)

There is no third integer length ~c~ such that 5, 1, ~c~ can form a right angled triangle.

