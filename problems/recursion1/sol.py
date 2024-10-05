import math

MOD = int(1e9+7)

matrix = [
    [1, 1],
    [1, 0]
]

def mat_mult(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for x in range(len(m1)):
        for y in range(len(m2[0])):
            res = 0
            for a in range(len(m2)):
                res += m1[x][a] * m2[a][y]
                res = res % MOD
            result[x][y] = res
    return result

def exponentiate(mat, p):
    cur_val = [[int(i1==i2) for i2 in range(len(mat[0]))] for i1 in range(len(mat))]
    cur_power = mat
    for shift in range(2+math.floor(math.log2(p))):
        if (1 << shift) & p:
            cur_val = mat_mult(cur_val, cur_power)
        cur_power = mat_mult(cur_power, cur_power)
    return cur_val

n = int(input()) + 1
move = exponentiate(matrix, n)
moved = mat_mult(move, [[1], [0]])
print(int(moved[1][0]))
