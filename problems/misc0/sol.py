a, b = list(map(int, input().split()))

# Simple lcm work.
for x in range(2, min(a, b)):
    while a % x == 0 and b % x == 0:
        a //= x
        b //= x

# 1/b is the jump size.
if b % 2 == 0:
    print("Other axis!")
else:
    print("Free!")
