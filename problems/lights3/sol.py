import sys
import math

n = int(input())

# sqrt(n) + sqrt(n/2) + sqrt(n/4) + ...
# but powers of 2 cause double counting.

total = math.floor(math.sqrt(n)) + math.floor(math.sqrt(n//2))
print(total)
