Bella is playing the new hit game Excavate-Fabricate, centered around placing various cubes in interesting configurations.
One of the characters in this game is the villager, which can trade both gold and unique items.

The inventory for this game however is slightly restricted - **You can only hold 1 of every unique item in the game** (Excluding gold, of which you can hold infinite). This game does allow you to have negative gold, but the final score of the game is based on how much gold you acquire, and so Bella wants to get rich quick.

Bella wants to figure out if the trading system is exploitable. The system is exploitable, if there exists some inventory that Bella can start with, so that after some trading, Bella can end up with the same inventory she started with, except she now has more gold.

If Bella ends up with her starting inventory after ~s~ turns, then the game is ~s~-exploitable.

## Input

Input will start with a single integer, ~T~, the number of test cases.
For each test case, input starts with a two space-separated integers, ~N~ and ~M~, the number of unique items, and the number of trades the villager has on offer.
~N~ lines follow, each containing the name of a unique item. These names are comprised solely of lowercase english letters.
After this ~M~ lines follow, in the format:

```
item1 item2 and x gold can be traded for item3 item4 and y gold
```

This means that if you have item1, item2, you can remove ~x~ gold, item1 and item2 from your inventory, and receive ~y~ gold, item3 and item4. (If you already have item3 or item4 they can simply be discarded).

* Trades can have different numbers of unique items (including 0). This might look like `and x gold can be traded for and y gold`. This doesn't make sense in english but is easier to parse.
* ~x~ and ~y~ can both be 0.
* Items that appear in the left hand side can also appear in the right hand side simultaneously. This can be thought of as a requirement to do the trade ("I'll trade you 6 gold for a leather hide only if you already have the leathermakers outfit.")

## Output

For each test case:

If the game is not exploitable, output `0`.

If the game is exploitable, output the smallest positive integer ~s~ for which the game is ~s~-exploitable.

## Constraints

* ~1 \leq T \leq 10~
* ~1 \leq N \leq 7~
* ~1 \leq M \leq 300~
* ~0 \leq x, y \leq 10^4~ (`x` and `y` being the amounts of gold in each trade)

Each unique item name will be one of the following:

```
amulet
sword
axe
armor
poison
dirt
steel
```

## Sample tests

Input:
```
2
3 5
sword
axe
armor
and 1 gold can be traded for axe and 0 gold
axe and 2 gold can be traded for sword and 0 gold
axe sword and 3 gold can be traded for armor and 0 gold
sword armor axe and 0 gold can be traded for and 21 gold
armor axe and 0 gold can be traded for armor and 1 gold
2 3
poison
steel
and 1 gold can be traded for poison and 0 gold
poison and 1 gold can be traded for steel and 0 gold
steel and 0 gold can be traded for poison and 1 gold
```

Output:
```
8
0
```

Explanation:
In the first example, we can start with nothing, and use:

* Trade 1 to get an axe (-1 gold)
* Trade 2 to get a sword with our axe (-3 gold)
* Trade 1 to get an axe (-4 gold)
* Trade 3 to get armor with our sword + axe (-7 gold)
* Trade 1 to get an axe (-8 gold)
* Trade 2 to get a sword with our axe (-10 gold)
* Trade 1 to get an axe (-11 gold)
* Trade 4 to get 21 gold with all of our items (+10)

And so after 8 trades, we have nothing, but have gained 10 gold.

In the second example, the system is not exploitable (We can trade poison for steel and vice-versa, but the net gold change is 0).
