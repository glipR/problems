import math

n, m = list(map(int, input().split()))

l2n, l2m = math.floor(math.log2(n)), math.floor(math.log2(m))

if l2n == l2m:
    print("2nd Player")
elif l2n > l2m:
    print("Vaughn")
else:
    print("Hazel")
