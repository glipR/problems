from decimal import Decimal, getcontext

getcontext().prec = 50

n = int(input())

m = max(100,int(n**0.5))
m1 = n//m

total = Decimal("0")

# Handle the first m columns
for i in range(1, m+1):
    total += Decimal(n//i)/Decimal(i)
# Handle the remaining m1 rows
for i in range(1, m1+1):
    total += Decimal.ln(Decimal(n//i) / Decimal(m)) + Decimal(1) / Decimal(2 * (n//i)) - Decimal(1) / Decimal(2 * m)

print(total)
