# Consider all numbers to 2^n
# 000 F
# 001 T
# 010 F
# 011 T
# 100 T
# 101 T
# 110 F
# 111 T

# 1/2 end with 1: True
# 1/4 end with 10: False
# 1/8 end with 100: True

# For 2^n, #True is 2^(n-1) + 2^(n-3) + 2^(n-5) + ...
# For the remaining, keep track of whether to add the 1 or not.

import math

n = int(input())
l2 = math.floor(math.log2(n))
turned = 0
cur = 0
for power in range(l2, -1, -1):
    if cur + (1 << power) <= n:
        add_0 = power % 2 == 0
        tmp = turned
        for shift in range(power-1, -1, -2):
            turned += 1 << shift
        turned += add_0
        # print(f"2^{power} contributes {turned - tmp}. {add_0}")
        cur += 1 << power

print(turned)
