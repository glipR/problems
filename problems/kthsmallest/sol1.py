def get_print(queue, i):
    print(f"VAL {queue} {i}")
    return int(input())

def solve(queues, k, max_val, get_val_method=get_print):
    DP = {}
    def get_val(queue, i):
        if (queue, i) in DP:
            return DP[(queue, i)]
        if i == 0:
            return float("-inf")
        DP[(queue, i)] = get_val_method(queue, i)
        return DP[(queue, i)]

    los = [0 for _ in range(queues)] # What is guaranteed in the zone?
    his = [k for _ in range(queues)] # What is guaranteed out of the zone after?
    n_solved = 0

    cur_stored = [None]*queues
    # Start by grabbing k+1 equally distributed.
    for queue in range(1, queues+1):
        i = (k+1) // queues + (1 if (k+1) % queues >= queue else 0)
        v = get_val(queue, i)
        cur_stored[queue-1] = (v, i)

    # Now, repeatedly shrink the search size.
    while n_solved < queues:
        # print("LO",los)
        # print("HI",his)
        # Find the smallest and largest unsolved portions
        min_val, max_val = (float("inf"), -1), (float("-inf"), -1)
        for i in range(queues):
            if his[i] - 1 > los[i]: # unsolved
                min_val = min(min_val, (cur_stored[i][0], i))
                max_val = max(max_val, (cur_stored[i][0], i))
        # print(min_val, max_val)
        if min_val == max_val:
            # 1 left unsolved. We know total is k
            ind = min_val[1]
            los[ind] = cur_stored[ind][1]-1
            his[ind] = los[ind]+1
            n_solved += 1
            break
        # We know that min_val *is* in the k smallest.
        # We know that max_val *is not* in the k smallest.
        mini = min_val[1]
        maxi = max_val[1]
        los[mini] = cur_stored[mini][1]
        his[maxi] = cur_stored[maxi][1]
        # Now shift the two, so that we maximise the smallest unsolved portion.
        d1 = his[mini] - los[mini]
        d2 = his[maxi] - los[maxi]
        min_dist = min(d1, d2)
        if min_dist > 1:
            # We can safely just shift.
            cur_stored[mini] = (get_val(mini+1, los[mini] + min_dist // 2), los[mini] + min_dist // 2)
            cur_stored[maxi] = (get_val(maxi+1, his[maxi] - min_dist // 2), his[maxi] - min_dist // 2)
        else:
            # One or both of these are solved.
            if d2 != 1: # and so d1 == 1
                # Easy - just leave it as is.
                n_solved += 1
                continue
            elif d2 == 1:
                n_solved += 1
                if d1 == 1:
                    n_solved += 1
                cur_stored[maxi] = (get_val(maxi+1, his[maxi] - 1), his[maxi] - 1)
                # We need to find another unsolved one to bump up
                for i2 in range(queues):
                    if his[i2] - 1 > los[i2]: # unsolved
                        if cur_stored[i2][1] < his[i2] - 1:
                            cur_stored[i2] = (get_val(i2+1, cur_stored[i2][1]+1), cur_stored[i2][1]+1)
                            break
                else:
                    # Nothing can increase. This means that we already have our k vals.
                    for i2 in range(queues):
                        if his[i2] - 1 > los[i2]: # unsolved
                            los[i2] = cur_stored[i2][1]
                            his[i2] = los[i2] + 1
                            n_solved += 1

    vals = [(get_val(i+1, los[i]), i+1, los[i]) for i in range(queues)]
    mval = max(vals)
    return mval[1], mval[2]

if __name__ == "__main__":
    queues, k, max_val = list(map(int, input().split()))
    res = solve(queues, k, max_val, get_val_method=get_print)
    print(f"ANS {res[0]} {res[1]}")
