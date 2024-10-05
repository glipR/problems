def solve(coins):
    if len(coins) == 1:
        return coins[0]
    if len(coins) == 2:
        print(f"TEST {coins[0]} | {coins[1]}")
        res = input()
        if res == "LEFT":
            return coins[0]
        elif res == "RIGHT":
            return coins[1]
        else:
            raise ValueError()
    amount = len(coins) // 3
    coin_left = coins[:amount]
    coin_right = coins[amount:2*amount]
    coin_extra = coins[2*amount:]
    print(f"TEST {' '.join(map(str, coin_left))} | {' '.join(map(str, coin_right))}")
    res = input()
    if res == "LEFT":
        return solve(coin_left)
    elif res == "RIGHT":
        return solve(coin_right)
    elif res == "EQUAL":
        return solve(coin_extra)

n = int(input())

coins = list(range(1, n+1))

coin = solve(coins)
print("ANS", coin)
