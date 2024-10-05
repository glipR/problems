def guess(c1, c2, c3):
    print("TEST", " ".join(map(str, c1)), "|", " ".join(map(str, c2)), "|", " ".join(map(str, c3)))
    return [
        list(map(int, section.strip().split()))
        for section in input().split(">")
    ]

def solve_1(coins):
    # log_4(n)
    if len(coins) == 1:
        return coins[0]
    elif len(coins) == 2:
        res = guess(coins[:1], coins[1:], [])
        assert len(res) == 3
        if res[0][0] == 1:
            return coins[0]
        else:
            return coins[1]
    amount = (len(coins) + 1) // 4
    coin1 = coins[:amount]
    coin2 = coins[amount:2*amount]
    coin3 = coins[2*amount:3*amount]
    coin4 = coins[3*amount:]
    res = guess(coin1, coin2, coin3)
    assert len(res) != 3
    if len(res) == 2:
        # The heavier one is alone.
        if res[0][0] == 1:
            return solve_1(coin1)
        if res[0][0] == 2:
            return solve_1(coin2)
        if res[0][0] == 3:
            return solve_1(coin3)
    else:
        # All are equal, the remainder is the culprit.
        return solve_1(coin4)

def solve_2(coins):
    if len(coins) == 2:
        return coins[0], coins[1]
    elif len(coins) == 3:
        res = guess([coins[0]], [coins[1]], [coins[2]])
        cur = []
        if 1 in res[0]:
            cur.append(coins[0])
        if 2 in res[0]:
            cur.append(coins[1])
        if 3 in res[0]:
            cur.append(coins[2])
        return cur[0], cur[1]
    elif len(coins) in [4, 5]:
        res = guess([coins[0]], [coins[1]], [coins[2]])
        assert len(res) != 3
        if len(res) == 1:
            return solve_2(coins[3:])
        cur = []
        if 1 in res[0]:
            cur.append(coins[0])
        if 2 in res[0]:
            cur.append(coins[1])
        if 3 in res[0]:
            cur.append(coins[2])
        if len(cur) == 1:
            cur.append(solve_1(coins[3:]))
        return cur[0], cur[1]

    # At least 6, so 3*coin4 <= len
    amount = (len(coins)+2) // 4

    coin1 = coins[:amount]
    coin2 = coins[amount:2*amount]
    coin3 = coins[2*amount:3*amount]
    coin4 = coins[3*amount:]
    res = guess(coin1, coin2, coin3)
    assert len(res) != 3
    if len(res) == 2:
        if len(res[0]) == 2:
            # 1-1-0
            cur = []
            if 1 in res[0]:
                cur.append(solve_1(coin1))
            if 2 in res[0]:
                cur.append(solve_1(coin2))
            if 3 in res[0]:
                cur.append(solve_1(coin3))
            return cur[0], cur[1]
        else:
            # 2-0-0-0, or 1-0-0-1
            if res[0][0] == 1:
                weighted_first = coin1 + coin2 + coin3
            elif res[0][0] == 2:
                weighted_first = coin2 + coin3 + coin1
            elif res[0][0] == 3:
                weighted_first = coin3 + coin1 + coin2

            weighted = weighted_first[:len(coin4)]
            empty = weighted_first[len(coin4):2*len(coin4)]
            res2 = guess(weighted, empty, coin4)

            assert len(res2) == 2
            if len(res2[0]) == 2:
                return solve_1(weighted), solve_1(coin4)
            else:
                return solve_2(weighted)
    else:
        # 0-0-0-2
        return solve_2(coin4)

def solve_3(coins):
    if len(coins) == 3:
        return coins[0], coins[1], coins[2]
    elif len(coins) == 4:
        res = guess([coins[0]], [coins[1]], [coins[2]])
        if len(res) == 1:
            return coins[0], coins[1], coins[2]
        else:
            if 1 in res[1]:
                return coins[1], coins[2], coins[3]
            if 2 in res[1]:
                return coins[0], coins[2], coins[3]
            if 3 in res[1]:
                return coins[0], coins[1], coins[3]
    amount = len(coins) // 3
    coin1 = coins[:amount]
    coin2 = coins[amount:2*amount]
    coin3 = coins[2*amount:3*amount]
    coin4 = coins[3*amount:]

    res = guess(coin1, coin2, coin3)
    if len(res) == 3:
        # 2-1-0-0
        cur = []
        if res[0][0] == 1:
            cur.extend(solve_2(coin1))
        if res[0][0] == 2:
            cur.extend(solve_2(coin2))
        if res[0][0] == 3:
            cur.extend(solve_2(coin3))
        if res[1][0] == 1:
            cur.append(solve_1(coin1))
        if res[1][0] == 2:
            cur.append(solve_1(coin2))
        if res[1][0] == 3:
            cur.append(solve_1(coin3))
        return cur[0], cur[1], cur[2]
    elif len(res) == 2:
        if len(res[0]) == 2:
            # 1-1-0-1
            cur = []
            if 1 in res[0]:
                cur.append(solve_1(coin1))
            if 2 in res[0]:
                cur.append(solve_1(coin2))
            if 3 in res[0]:
                cur.append(solve_1(coin3))
            cur.append(solve_1(coin4))
            return cur[0], cur[1], cur[2]
        else:
            # 3-0-0-0
            # 2-0-0-1
            # 1-0-0-2
            cur = coin4
            if res[0][0] == 1:
                cur.extend(coin1)
            if res[0][0] == 2:
                cur.extend(coin2)
            if res[0][0] == 3:
                cur.extend(coin3)
            # log_3(n)
            return solve_3(cur)
    else:
        # 0-0-0-3 - not possible due to definition of amount.
        # 1-1-1-0
        return solve_1(coin1), solve_1(coin2), solve_1(coin3)

n = int(input())

a, b, c = solve_3(list(range(1, n+1)))
print("ANS", a, b, c)
