n, m = list(map(int, input().split()))

triangle = (m * (m-1)) // 2

total = triangle * (n // m)
extra = n % m
total += (extra * (extra + 1)) // 2

print(total)

