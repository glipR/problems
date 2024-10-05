t = int(input())

for _ in range(t):
    n = int(input())
    values = [None]*(2*n)
    for x in range(1, 2*n, 2):
        print(x, x+1)
        a, b, s = input().split()
        s = int(s)
        if s == 1:
            break
        values[x-1] = a
        values[x] = b
    if s == 1:
        continue
    indicies = {}
    for x in range(2*n):
        if values[x] not in indicies:
            indicies[values[x]] = []
        indicies[values[x]].append(x)
    for i1, i2 in indicies.values():
        print(i1+1, i2+1)
        a, b, s = input().split()
        if int(s) == 1:
            break
