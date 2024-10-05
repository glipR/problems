t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    diffs = [arr[i+1] - arr[i] for i in range(n-1)]

    def can_do(v):
        if len(diffs) == 0:
            return True
        if v == 0:
            return sum(diffs) == 0
        cnt = 0
        for d in diffs:
            if d > 0:
                cnt += (d-1) // v

        return cnt <= k

    lo = -1
    hi = max(diffs) if diffs else 10
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if can_do(mid):
            hi = mid
        else:
            lo = mid
    print(hi)
