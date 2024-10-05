import random

# Sample
with open("tests/1.in", "w") as f:
    f.write("""2 7\n""")

for x in range(2, 16):
    with open(f"tests/{x}.in", "w") as f:
        J = random.randint(1, 10**10)
        M = random.randint(1, 10**10)
        f.write(f"{J} {M}\n")

