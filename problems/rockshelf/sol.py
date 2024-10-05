T = int(input())

def z_array(s):
    z = [len(s)-1]*len(s)
    L = 0
    R = 0
    for i in range(1, len(s)):
        j = max(min(z[i-L], R-i), 0)
        while i+j<len(s) and s[i+j] == s[j]:
            j += 1
        z[i] = j
        if (i + z[i] > R):
            R  = i + z[i]
            L = i
    return z

for _ in range(T):
    n = int(input())
    top = list(map(int, input().split()))
    mid = list(map(int, input().split()))
    bot = list(map(int, input().split()))
    positions = [(x, "t") for x in top[1:]] + [(x, "m") for x in mid[1:]] + [(x, "b") for x in bot[1:]] 
    positions.sort()
    if len(positions) == 0:
        print(n-1)
        continue
    distances = [(n - positions[-1][0] + positions[0][0], positions[0][1])]
    for x in range(len(positions)-1):
        distances.append((positions[x+1][0] - positions[x][0], positions[x+1][1]))
    z = z_array(distances + distances)
    same_as = 0
    for x in range(len(distances)-1):
        if z[x+1] == 2*len(distances) - x - 1:
            same_as += 1
    print(same_as)

