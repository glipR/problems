a = int(input())

res = 0
for x in range(1, a+1):
    for y in range(x, a+1):
        if y % x == 0:
            res += 1/x

print(res)
