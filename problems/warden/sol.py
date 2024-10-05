start = input()

if start == "0":
    state = input()
    bit = int(input()) - 1
    # Compute board bits.
    vec = [0, 0, 0]
    want = [bit & 1 != 0, bit & 2 != 0, bit & 4 != 0]
    for jump in [0, 1, 2]:
        for x in range(8):
            if x & (1 << jump) and state[x] == "x":
                vec[jump] += 1
        vec[jump] %= 2
    diff = [vec[x] ^ want[x] for x in range(3)]
    num = 0
    for x in range(3):
        num += diff[x] * (1 << x)
    print(num + 1)
elif start == "1":
    state = input()
    vec = [0, 0, 0]
    for jump in [0, 1, 2]:
        for x in range(8):
            if x & (1 << jump) and state[x] == "x":
                vec[jump] += 1
        vec[jump] %= 2
    num = 0
    for x in range(3):
        num += vec[x] * (1 << x)
    print(num + 1)
else:
    pass