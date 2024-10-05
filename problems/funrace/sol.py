n = int(input())
nums = sorted(list(map(int, input().split())))

# print(nums)

rp = -1

best = 0
best_indicies = (-1, -1)

for lp in range(n):
    rp = max(rp, lp)
    while rp < n - 1 and nums[rp+1] - nums[rp] < 5:
        rp += 1
    # Consider everything from lp to rp.
    if rp - lp + 1 > best:
        best = rp - lp + 1
        best_indicies = (lp, rp)

print(best, nums[best_indicies[0]], nums[best_indicies[1]])
