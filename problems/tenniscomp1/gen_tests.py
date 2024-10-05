import random

with open("tests/1.in", "w") as f:
    f.write("""4
name1 4
name2 7
name3 2
name4 10
""")

# Edge case - size 2 and lexicographic comparison
with open("tests/2.in", "w") as f:
    f.write("""2
s3 4
s1 4
""")


def random_name():
    l = random.randint(5, 20)
    return "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(l)])

competitor_options = [1024, 512, 256]
skill_options = [random.randint(1, pow(10, 9)) for _ in range(700)]
people_names = list(set(random_name() for _ in range(3000)))
# Just random should suffice here.
for x in range(3, 11):
    with open(f"tests/{x}.in", "w") as f:
        competitors = random.choice(competitor_options)
        f.write(f"{competitors}\n")
        random.shuffle(people_names)
        for y in range(competitors):
            f.write(f"{people_names[y]} {random.choice(skill_options)}\n")
