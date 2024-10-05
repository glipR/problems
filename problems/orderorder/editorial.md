This problem was primarily an implementation question which tested your ability to parse and print complex strings.

You can solve this using a hashmap (dictionary) to keep track of the number of times a particular food is brought up for a particular meal. For example, the key ('dinner', 'ragu') can map to the number of times ragu has been ordered for dinner.

The final snag in the implementation is the "I'll have the previous!" request. This can be solved by keeping a variable to keep track of the last legitimate order made by a patron, and setting this each time a new order is made.

A neat trick you can use for these problems is that the `re` module is included in the python standard library, so you can avoid a lot of the string matching pain by using regex:

Here's some snippets from the implementation:

```python
# Regex patterns for the orders.
patterns = [re.compile(rf"For my {course} can I get (.*)") for course in courses]

    # I'll have that too...
    if line == "I'll get that too, please!":
        item = prev_item
        course = prev_course

    # Order logic (can be done with defaultdict if you like)...
    if item not in items[course]:
        items[course][item] = 0
    items[course][item] += 1

    prev_item = item
    prev_course = course
```
