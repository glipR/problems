import sys
import math
from decimal import Decimal, getcontext

getcontext().prec = 50

a = int(input())

# Subtract 1 for the trail off
res = Decimal(a) * Decimal(math.pi) * Decimal(math.pi) / Decimal(6) - 1

print("Pretty good approximation:", res, file=sys.stderr)

ceil = min(a, int(1e6))

# Now, we need to reduce by a%x/x for all x <= a.
# After which, our error term will be 1 + 2log(a)log(1+log(a)/a)
for x in range(1, a // ceil):
    reduction = 1 - Decimal(x) * Decimal.ln(Decimal((x+1))/Decimal(x))
    # print(f"1/{a//x}^2 + ... + {a//(x+1)}/{a//(x+1)}^2 = {reduction}")
    res -= reduction

# Below sqrt(a), we can manually subtract the value
for x in range(2, ceil):
    res -= Decimal(a % x) / Decimal(x*x)

print("Better:", res, file=sys.stderr)

print(res)
