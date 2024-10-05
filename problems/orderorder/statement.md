## Statement

Ed & James host a busy and bustling restaurant. In this restaurant, as with most, orders are taken at a blistering pace, and often out of order.

As the waiter, you've been tasked with deciphering this flurry of orders into a neat list at the end so the chefs know what to cook.

Patrons around the table will shout their preffered starter, main, side, and dessert in no particular order, and it's your job to itemise the tables order in full.

## Input/Output

Input will start with a single integer ~n~, the number of incoming requests.

~n~ lines will follow, each containing a phrase of the sort: `For my <starter/main/side/dessert> can I get <food>`. The only other line that might be included is `I'll get that too, please!`. This means the previous line order should be repeated.

Output start with `Let me repeat your order...` should contain an itemized list of the starters, mains, sides and desserts, so as to only report the amount of servings for each food. If no items are ordered for a particular meal, then `  Nothing` should be printed (note the two spaces)

For items of a particular course, these should be listed like `* <amount>x <food>`, and these should be listed in `<amount>` descending. If two meals have the same amount ordered, these should be ordered to be lexicographically increasing.

This format should be followed exactly. Use the following example as a guide:

For input:
```
9
For my main can I get Malatang
For my starter can I get Tofu Jianbing
For my main can I get Malatang
For my main can I get Penne pasta
For my dessert can I get Mars Bar
For my main can I get Youpo Chemian
I'll get that too, please!
For my dessert can I get Sponge Roll with Vanilla Icecream
For my starter can I get Pepper Crunch Sandwich
```

Should result in the output:
```
Let me repeat your order...
For Starter:
* 1x Pepper Crunch Sandwich
* 1x Tofu Jianbing
For Main:
* 2x Malatang
* 2x Youpo Chemian
* 1x Penne pasta
For Side:
  Nothing
For Dessert:
* 1x Mars Bar
* 1x Sponge Roll with Vanilla Icecream
```

And any variation from this response would give the wrong answer.

## Constraints

* ~1 \leq n \leq 100~
* Each line of input will be at most 100 characters in length.
