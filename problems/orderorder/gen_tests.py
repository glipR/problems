import random

def random_meal():
    length = random.randint(3, 40)
    return "".join(random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(length))

repeat_chance = 0.2

# All one course and multiple repeats. Meal name contains course name
with open("tests/1_1.in", "w") as f:
    f.write("""5
For my side can I get starter
I'll get that too, please!
I'll get that too, please!
For my side can I get main
I'll get that too, please!
""")

# Meals in multiple courses
with open("tests/1_2.in", "w") as f:
    f.write("""8
For my side can I get A
I'll get that too, please!
For my starter can I get B
For my starter can I get D
For my main can I get B
For my main can I get B
For my dessert can I get A
For my dessert can I get D
""")

for x in range(3, 11):
    n = random.randint(50, 100)
    meals = list(set(random_meal() for _ in range(n//8)))

    lines = []
    lines.append(str(n) + "\n")

    for y in range(n):
        if y != 0 and random.random() < repeat_chance:
            lines.append("I'll get that too, please!\n")
            continue
        course = random.choice(["starter", "main", "side", "dessert"])
        meal = random.choice(meals)

        lines.append(f"For my {course} can I get {meal}\n")

    with open(f"tests/1_{x}.in", "w") as f:
        f.writelines(lines)
