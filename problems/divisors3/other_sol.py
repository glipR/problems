import sys
import math
from decimal import Decimal, getcontext

getcontext().prec = 50

n = int(input())

# Subtract 1 for the trail off
res = Decimal(n) * Decimal(math.pi) * Decimal(math.pi) / Decimal(6) - 1

print("Pretty good approximation:", res, file=sys.stderr)

ceil = min(n, int(1e6))

# Now, we need to reduce by a%d/d^2 for all d <= a.
for d in range(1, n // ceil):
    d = Decimal(d)
    smol = Decimal(n // (d + 1))
    beeg = Decimal(n // d)
    first_part = d * smol + (n % beeg) + d * (beeg - smol - 1)
    second_part = Decimal(1) / Decimal(smol - 1) - Decimal(1) / Decimal(beeg - 1)
    third_part = Decimal.ln((beeg - 1) / (smol - 1)) + Decimal(1) / (2 * (beeg - 1)) - Decimal(1) / (2 * (smol - 1))

    reduction = first_part * second_part - d * third_part
    # print(f"1/{n//d}^2 + ... + {n//(d+1)}/{n//(d+1)}^2 = {reduction}")
    res -= reduction

# Below sqrt(a), we can manually subtract the value
for d in range(2, ceil):
    res -= Decimal(n % d) / Decimal(d*d)

print("Better:", res, file=sys.stderr)

print(res)
