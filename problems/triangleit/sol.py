import math

t = int(input())

def is_sqrt(x):
    # returns False if not a sqrt, otherwise the sqrt.
    possible = math.floor(math.sqrt(x) + 0.5)
    # and possible ensures that 0 returns False.
    return possible**2 == x and possible

for case in range(1, t+1):
    # Read two integers
    a, b = list(map(int, input().split()))
    # sqrt(pos1)^2 = a^2 + b^2 is a triple.
    pos1 = a**2 + b**2
    # sqrt(pos2)^2 + b^2 = a^2 is a triple (or vice versa).
    pos2 = abs(a**2 - b**2)
    p1, p2 = is_sqrt(pos1), is_sqrt(pos2)
    # 0 is never printed in this case.
    if p1:
        print(p1)
    elif p2:
        print(p2)
    else:
        print(-1)
