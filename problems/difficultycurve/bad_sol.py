t = int(input())

for case in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    diffs = [arr[i+1] - arr[i] for i in range(n-1)]
    diffs.sort()
    if not diffs or diffs[-1] == 0:
        print(0)
        continue
    extras = []
    done = False
    for _ in range(k):
        # Break largest remaining portion into two parts.
        if extras and ((diffs == []) or extras[-1] >= diffs[-1]):
            if extras[-1] == 1:
                print(1)
                done = True
                break
            s1 = extras[-1] // 2
            s2 = (extras[-1] + 1) // 2
            extras.pop()
            extras.append(s1)
            extras.append(s2)
            extras.sort()
        else:
            if diffs[-1] == 1:
                print(1)
                done = True
                break
            s1 = diffs[-1] // 2
            s2 = (diffs[-1] + 1) // 2
            diffs.pop()
            extras.append(s1)
            extras.append(s2)
            extras.sort()
    if not done:
        m = -1
        if extras:
            m = max(m, extras[-1])
        if diffs:
            m = max(m, diffs[-1])
        print(m)

            