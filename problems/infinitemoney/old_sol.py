import sys
INPUT1_MATRIX = [[0 for x in range(300)] for y in range(300)]
INPUT2_MATRIX = [[0 for x in range(300)] for y in range(300)]
RESULT_MATRIX = [[0 for x in range(300)] for y in range(300)]
ORIGINAL_MATRIX = [[0 for x in range(300)] for y in range(300)]

n = 300

def exponentiate(power):
    for x in range(n):
        for y in range(n):
            INPUT1_MATRIX[x][y] = -1000000000 if x != y else 0
    for x in range(n):
        for y in range(n):
            INPUT2_MATRIX[x][y] = ORIGINAL_MATRIX[x][y]
    while (power):
        if (power & 1):
            for x in range(n):
                for y in range(n):
                    maximum = -1000000000
                    for z in range(n):
                        maximum = max(INPUT1_MATRIX[x][z] + INPUT2_MATRIX[z][y], maximum)
                    RESULT_MATRIX[x][y] = maximum
            for x in range(n):
                for y in range(n):
                    INPUT1_MATRIX[x][y] = RESULT_MATRIX[x][y]
        for x in range(n):
            for y in range(n):
                maximum = -1000000000
                for z in range(n):
                    maximum = max(INPUT2_MATRIX[x][z] + INPUT2_MATRIX[z][y], maximum)
                RESULT_MATRIX[x][y] = maximum
        for x in range(n):
            for y in range(n):
                INPUT2_MATRIX[x][y] = RESULT_MATRIX[x][y]
        power //= 2
    for x in range(n):
        for y in range(n):
            RESULT_MATRIX[x][y] = INPUT1_MATRIX[x][y]

n, m = [int(x) for x in input().split()]

for x in range(n):
    for y in range(n):
        ORIGINAL_MATRIX[x][y] = -1000000000 if x != y else 0

for _ in range(m):
    i, j, cij, cji = [int(x) for x in input().split()]
    ORIGINAL_MATRIX[i-1][j-1] = cij
    ORIGINAL_MATRIX[j-1][i-1] = cji

# Just be safe.
exponentiate(2*n)
for x in range(n):
    if RESULT_MATRIX[x][x] > 0:
        # loop found.
        break
else:
    print(0)
    sys.exit(0)

hi = 2 * n
lo = 0
while hi - lo > 1:
    mid = (hi + lo) // 2
    exponentiate(mid)
    # print(mid, [[RESULT_MATRIX[x][y] for y in range(n)] for x in range(n)])
    for x in range(n):
        if RESULT_MATRIX[x][x] > 0:
            # loop found.
            hi = mid
            break
    else:
        lo = mid

# hi should be the lowest time that a loop exists.
print(hi)
