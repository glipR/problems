import math

MOD = int(1e9+7)

matrix = [
    [1, 1, 0, 0, 0, 0, 0], # fn+2
    [1, 0, 0, 0, 0, 0, 0], # fn+1
    [1, 0, 1, 0, 0, 0, 0], # bn+2
    [0, 0, 1, 1, 0, 0, 0], # cn+1
    [0, 0, 0, 1, 0, 0, 0], # cn
    [0, 0, 0, 1, 0, 1, 0], # dn
    [0, 0, 0, 0, -1, 2, 4], #hn
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
    for shift in range(2+math.floor(math.log2(p+1))):
        if (1 << shift) & p:
            cur_val = mat_mult(cur_val, cur_power)
        cur_power = mat_mult(cur_power, cur_power)
    return cur_val

n = int(input())
move = exponentiate(matrix, n)

col = [[2], [1], [2], [1], [0], [0], [0]]

moved = mat_mult(move, col)
print(int(moved[6][0]))

# 0, 1, 9, 51
# 4*0 + 1 * F(1) = 1 OR 2*1-1
# 4*1 + 4 * F(1) + 1 * F(2) = 9
# 4*9 + 9 * F(1) + 4 * F(2) + 1 * F(3) = 36 + 9 + 4 + 2 = 51
