nums = int(input())
v_and_p = list(map(lambda x: list(map(int, x.split("_"))), input().split()))
sort_keys = list(map(lambda x: (x[0]*x[1], x[0], x[1]), v_and_p))
sort_keys.sort()

formatted = list(map(lambda x: f"{x[1]}_{x[2]}", sort_keys))
print(" ".join(formatted))
