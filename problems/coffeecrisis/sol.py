days, specials = list(map(int, input().split()))

DAY, DURATION, STRENGTH, CAFFEINE, INDEX = range(5)

# Day, Duration, Strength, Caffeine
coffees = list(sorted([
    list(map(int, input().split())) + [i]
    for i in range(specials)
], key=lambda x:x[0]))

def binary_search(time):
    """Find the first special coffee that can be bought on day >= `time`."""
    lo = -1
    hi = len(coffees)-1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if coffees[mid][DAY] >= time:
            hi = mid
        else:
            lo = mid
    if coffees[hi][DAY] >= time:
        return hi
    return None

# DP[i] = # of assignments that can be completed from time coffees[i][0].
DP = [None] * len(coffees)
used_coffee = [None] * len(coffees)
# Set up base case.
ind = -1
# Option 1: Do not take the coffee
DP[ind] = days - coffees[ind][DAY] + 1
# Option 2: Take the coffee (Stopping at the final day)
# The assignments the first coffee gives us
assignments = coffees[ind][STRENGTH] * min(days - coffees[ind][DAY] + 1, coffees[ind][DURATION]) 
# The delay this coffee stops us from getting others
delay = max(coffees[ind][DURATION], coffees[ind][CAFFEINE])
# The extra caffeine we can get from later days
extra = max(days - coffees[ind][DAY] + 1 - delay, 0)
DP[ind] = max(DP[ind], assignments + extra)
used_coffee[ind] = DP[ind] == assignments + extra

for ind in range(len(DP)-2, -1, -1):
    # Option 1: Do not take the coffee
    assignments = coffees[ind+1][DAY] - coffees[ind][DAY]
    DP[ind] = DP[ind+1] + assignments
    # Option 2: Take the coffee
    assignments = coffees[ind][STRENGTH] * min(days - coffees[ind][DAY] + 1, coffees[ind][DURATION]) 
    delay = max(coffees[ind][DURATION], coffees[ind][CAFFEINE])
    # Find the earliest special coffee after the delay
    ind2 = binary_search(coffees[ind][DAY] + delay)
    if ind2 is not None:
        extra = coffees[ind2][DAY] - (coffees[ind][DAY] + delay)
        DP[ind] = max(DP[ind], assignments + extra + DP[ind2])
        used_coffee[ind] = DP[ind] == assignments + extra + DP[ind2] 
    else:
        extra = max(days - (coffees[ind][DAY] + delay) + 1, 0)
        DP[ind] = max(DP[ind], assignments + extra)
        used_coffee[ind] = DP[ind] == assignments + extra

# Final bit, we can buy normal coffees before first special one
result = DP[0] + coffees[0][DAY] - 1
coffees_used = []
cur = 0
while cur is not None and cur != len(coffees):
    if used_coffee[cur]:
        coffees_used.append(coffees[cur][INDEX])
        delay = max(coffees[cur][DURATION], coffees[cur][CAFFEINE])
        cur = binary_search(coffees[cur][DAY] + delay)
    else:
        cur += 1

# print([c[DAY] for c in coffees])
# print(DP)
# print(used_coffee)

punchcard = ["-"] * len(coffees)
for ind in coffees_used:
    punchcard[ind] = "*"

print(result)
print("".join(punchcard))
