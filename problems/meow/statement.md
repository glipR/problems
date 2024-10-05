<img src="https://blog.monashicpc.com/new_binder/assets/img/comp_assets/mocha.jpg" alt="mocha_the_cat" width="180"/>

Mocha the cat (pictured above, silent but preparing to meow) likes to make noise. Lots of noise.

We've categorised the noises he makes as follows:

* `meow`: This is represented in text as `m`, followed by some non-zero amount of `e`s, a single `o`, and some non-zero amount of `w`s.
* `purr`: This is represented in text as `pu`, followed by at least 2 `r`s.
* `roar`: This is represented in text as `r`, followed by some non-zero amount of `o`s, followed by `ar`.

We want you to write a program to recognise these.

## Input

Input will being with a single integer ~T~, the number of test cases.
After this ~T~ lines will follow. Each line will contain a single string ~s~, with no whitespace.

## Output

If ~s~ is a `meow`, `purr`, or `roar`, print `meow`, `purr` or `roar`.
If ~s~ is none of these, then print `human noises`.

## Constraints

* ~1 \leq T \leq 20~
* ~1 \leq |s| \leq 30~

## Example

Input
```
7
roooar
meeeowwwwww
purrrrrr
roaar
pur
rmeow
hello
```

Output
```
roar
meow
purr
human noises
human noises
human noises
human noises
```

Explanation

The first 3 lines fit their respective definitions. 
* `roaar` repeats an `a` when it should not.
* `pur` needs at least 2 `r`s.
* `rmeow` contains an `r` when it should not.
* `hello` fits none of the 3 categories.
