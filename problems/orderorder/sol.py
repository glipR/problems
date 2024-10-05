# Courses
# * Starter
# * Main
# * Side
# * Drink
# * Dessert

import re

courses = [
    "starter",
    "main",
    "side",
    "dessert"
]

patterns = [re.compile(rf"For my {course} can I get (.*)") for course in courses]

items = {
    course: {}
    for course in courses
}

prev_course, prev_item = None, None

n = int(input())
for _ in range(n):
    line = input()
    for course, pattern in zip(courses, patterns):
        match_obj = pattern.match(line)
        if match_obj is not None:
            item = match_obj.group(1)
            break
    else:
        if line == "I'll get that too, please!":
            item = prev_item
            course = prev_course
        else:
            raise ValueError("Unmatched line")

    if item not in items[course]:
        items[course][item] = 0
    items[course][item] += 1

    prev_course, prev_item = course, item

print("Let me repeat your order...")
for course in courses:
    print(f"For {course[0].upper()}{course[1:]}:")
    course_items = list(items[course].keys())
    # Sort by amount decreasing, lexicographically increasing
    course_items.sort(key=lambda item: (-items[course][item], item))
    if course_items:
        for item in course_items:
            print(f"* {items[course][item]}x {item}")
    else:
        print(f"  Nothing")
