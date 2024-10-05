<img src="https://me.glipr.xyz/img/comp/diabolicaldefuser.png" alt="problem header" width="180"/>

You and 14 others have been kidnapped, and tied to a bomb! You've also been handcuffed, and your mouth is all taped up, and so you can't communicate, or interact with one another.

Each of you has a defuser tied to your back, which due to your restraints, everyone else can see but only you can access. Each defuser is equipped with two buttons, one which defuses the bomb and frees everyone, and one which explodes the bomb, killing everyone instantly.

Therefore, you only need one person to press the right button, but if anyone presses the wrong button, you all die. Of course, if no-one presses a button, you all die too. Luckily, for some reason the 15 of you knew this was going to happen, and had the time to come up with a strategy beforehand. But surely this will always be a 50/50 chance?

### Input

Input will begin with $T$, the number of test cases.

Each test case will begin with 14 lines, describing the defusers on everyone else's back.
These lines will be of the form `<name> has the defuser button on the <direction>`, where `<name>` is some string of lower-case a-to-z, and `<direction>` is either `left` or `right`.
For each test case, one final line of input is provided, in the form `Your name is <name>`, again `<name>` is some string of lower-case a-to-z.

### Output

For each test case, a single line of output should be produced.
This should be one of `left`, `right` or `pass`, depending on if you want to push your left button, your right button, or not press a button at all.

### Constraints

* $1 \leq T \leq 4000$

### Acceptance

Testing for this problem will be a bit different. 15 different processes will be launched, and test your program against each of the test cases from a different person's perspective. The results of these tests are then combined, and whether you survive this test case is calculated. You receive an `AC` verdict if you collectively survive 90% of tests, and receive a `WA` verdict otherwise. An optimal solution should have a 99.99% chance of receiving `AC`, so please do not resubmit
unless you are sure your strategy is optimal.

See the example run for an in-depth run-through of how tests will be run.

### Example Run

Suppose we want to test two situations, with two different sets of 15 people. The first set of people will be `onea`, `twoa`, `threea`, and so on, and the second set of people will be `oneb`, `twob`, `threeb`, and so on.

Then, your program will be ran 15 times. The first time, interaction will look like so:

Input
```
2
twoa has the defuser button on the left
threea has the defuser button on the right
foura has the defuser button on the right
...
fifteena has the defuser button on the left
Your name is onea
twob has the defuser button on the right
threeb has the defuser button on the left
fourb has the defuser button on the right
...
fifteenb has the defuser button on the left
Your name is oneb
```

Output
```
left
pass
```

The second time will look very similar, except you will be `twoa` and `twob` instead of `onea` and `oneb`.
The results of all 15 runs will be combined, and it is calculated whether you survive or not. You survive if someone does not respond pass, and if everyone who does not respond pass responds correctly (So in test 1, `twoa` responds `left`, or `threea` responds `right`...).
