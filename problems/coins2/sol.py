def solve_1(coins):
    # log_3(n)
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
        return solve_1(coin_left)
    elif res == "RIGHT":
        return solve_1(coin_right)
    elif res == "EQUAL":
        return solve_1(coin_extra)

def solve_2(coins):
    # 2*log_3(n)
    if len(coins) == 2:
        return coins
    amount = len(coins) // 3
    if 2 * amount < len(coins) - 2*amount:
        # This essentially just deals with 5.
        amount += 1
    coin_left = coins[:amount]
    coin_right = coins[amount:2*amount]
    coin_extra = coins[2*amount:]
    print(f"TEST {' '.join(map(str, coin_left))} | {' '.join(map(str, coin_right))}")
    res = input()
    if res == "LEFT":
        # Either 2-0-0
        # or 1-0-1.
        # Check by comparing half of extra against itself.
        # Some base cases for the second test:
        if len(coin_left) == 1:
            return solve_1(coin_left), solve_1(coin_extra)
        if len(coin_extra) == 1:
            print(f"TEST {coin_left[0]} | {coin_extra[0]}")
            res2 = input()
            if res2 == "LEFT":
                return solve_2(coin_left)
            elif res2 == "RIGHT":
                return solve_1(coin_left[1:]), solve_1(coin_extra)
            elif res2 == "EQUAL":
                # Since coin_left == 2
                return solve_1(coin_left[:1]), solve_1(coin_extra)
            return None
        # Now the meat and potatoes
        extra_amount = len(coin_extra) // 2
        extra_left = coin_extra[:extra_amount]
        extra_right = coin_extra[extra_amount:2*extra_amount]
        extra_extra = coin_extra[2*extra_amount:] # read all about it
        print(f"TEST {' '.join(map(str, extra_left))} | {' '.join(map(str, extra_right))}")
        res2 = input()
        if res2 == "LEFT":
            # 1-0-1-0
            return solve_1(coin_left), solve_1(extra_left)
        elif res2 == "RIGHT":
            # 1-0-0-1
            return solve_1(coin_left), solve_1(extra_right)
        elif res2 == "EQUAL":
            # 2-0-0-0 (plus extra_extra)
            return solve_2(coin_left + extra_extra)
    elif res == "RIGHT":
        # Either 0-2-0
        # or 0-1-1.
        # Check by comparing half of extra against itself.
        # Some base cases for the second test:
        if len(coin_right) == 1:
            return solve_1(coin_right), solve_1(coin_extra)
        if len(coin_extra) == 1:
            print(f"TEST {coin_right[0]} | {coin_extra[0]}")
            res2 = input()
            if res2 == "LEFT":
                return solve_2(coin_right)
            elif res2 == "RIGHT":
                return solve_1(coin_right[1:]), solve_1(coin_extra)
            elif res2 == "EQUAL":
                # Since coin_right == 2
                return solve_1(coin_right[:1]), solve_1(coin_extra)
            return None
        extra_amount = len(coin_extra) // 2
        extra_left = coin_extra[:extra_amount]
        extra_right = coin_extra[extra_amount:2*extra_amount]
        extra_extra = coin_extra[2*extra_amount:] # read all about it
        print(f"TEST {' '.join(map(str, extra_left))} | {' '.join(map(str, extra_right))}")
        res2 = input()
        if res2 == "LEFT":
            # 0-1-1-0
            return solve_1(coin_right), solve_1(extra_left)
        elif res2 == "RIGHT":
            # 0-1-0-1
            return solve_1(coin_right), solve_1(extra_right)
        elif res2 == "EQUAL":
            # 0-2-0-0 (plus extra_extra)
            return solve_2(coin_right + extra_extra)
    elif res == "EQUAL":
        # Either 1-1-0 or 0-0-2
        # Resolve by weighing all of extra against some subset of left+right
        not_extra = (coin_left + coin_right)[:len(coin_extra)]
        print(f"TEST {' '.join(map(str, coin_extra))} | {' '.join(map(str, not_extra))}")
        res2 = input()
        if res2 == "LEFT":
            # 0-0-2
            return solve_2(coin_extra)
        elif res2 == "RIGHT":
            return solve_1(coin_left), solve_1(coin_right)
        elif res2 == "EQUAL":
            # only 1-1-0 is possible, when n=5,
            return solve_1(coin_left), solve_1(coin_right)


n = int(input())

coins = list(range(1, n+1))

coin = solve_2(coins)
print("ANS", coin[0], coin[1])
