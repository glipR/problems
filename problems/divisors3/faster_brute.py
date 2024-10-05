from decimal import Decimal, getcontext

getcontext().prec = 40

a = int(input())

res = Decimal(0)
for x in range(1, a+1):
    res += Decimal(a//x)/Decimal(x)

print(res)
