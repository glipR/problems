import math
special, noccurences = list(map(int, input().split("_")))

# This occurs for number n*k.

nk = special * noccurences

nums = 0
for step in range(1, nk+1):
    nums += nk // step
    if nk % step == 0 and step > special:
        nums -= 1
print(nums)
