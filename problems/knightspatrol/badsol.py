possible_answers = ["0", "1"]
for _ in range(6):
    possible_answers = [p + "0" for p in possible_answers] + [p + "1" for p in possible_answers]

cindex = 0
for p in range(7):
    for _ in range(1 << 4):
        print(possible_answers[cindex], "0"*p + "1" + "0"*(7-p-1))
        cindex += 1
for _ in range(1 << 4):
    print(possible_answers[cindex], "1"*7)
    cindex += 1
