import sys
queues, k, max_val = list(map(int, input().split()))

DP = {}
def get_val(queue, i):
    if (queue, i) in DP:
        return DP[(queue, i)]
    print(f"VAL {queue} {i}")
    DP[(queue, i)] = int(input())
    return DP[(queue, i)]

def inner_binary(a):
    """Returns the number of values less than or equal to a."""
    # print(f"SEARCHING for <= {a}")
    total = 0
    max_less = (-float("inf"), None, None)
    for queue in range(1, queues+1):
        lo = 0
        hi = k+1
        while hi - 1 > lo:
            mid = (hi + lo + 1) // 2
            v = get_val(queue, mid)
            if v <= a:
                lo = mid
                max_less = max(max_less, (v, queue, mid))
            else:
                hi = mid
        total += lo
    return total, max_less

def outer_binary(max_val):
    lo = 0
    hi = max_val + 1
    while hi - 1 > lo:
        mid = (hi + lo) // 2
        total, max_val = inner_binary(mid)
        if total < k:
            lo = mid + 1
        elif total > k:
            hi = mid
        else:
            print(f"ANS {max_val[1]} {max_val[2]}")
            return
    # Now we know that there are duplicate correct answers.
    # The answer must be lo or hi.
    total_lo, max_val_lo = inner_binary(lo)
    total_hi, max_val_hi = inner_binary(hi)
    if total_lo >= k:
        print(f"ANS {max_val_lo[1]} {max_val_lo[2]}")
    else:
        print(f"ANS {max_val_hi[1]} {max_val_hi[2]}")


outer_binary(max_val)
