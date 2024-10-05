import random

with open("tests/1.in", "w") as f:
    f.write("0\n")

for x in range(2, 11):
    with open(f"tests/{x}.in", "w") as f:
        l = random.randint(1, 20000)
        # Select a random binary string of length l
        s = "".join([random.choice("01") for _ in range(l)])
        f.write(s + "\n")
