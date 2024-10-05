from functools import cache

MOD = int(1e9+7)

@cache
def fibonacci(n):
    if n <= 3:
        return [0, 1, 1, 2][n]
    m = n // 2
    if n%2 == 0:
        return (fibonacci(m+1)*fibonacci(m) + fibonacci(m)*fibonacci(m-1)) % MOD
    return (fibonacci(m+1)*fibonacci(m+1) + fibonacci(m)*fibonacci(m)) % MOD

print(fibonacci(int(input()) + 1))
