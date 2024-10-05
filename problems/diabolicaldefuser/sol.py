T = int(input())

def to_vec(x):
    vec = [0]*4
    for i in range(4):
        if (x+1) & (1 << i):
            vec[i]=1
    return vec

for _ in range(T):
    answers = [input().split() for __ in range(14)]
    me = input().split()[3]
    answers.append([me])
    answers.sort()
    rvec = [0]*4
    lvec = [0]*4
    for x in range(15):
        if len(answers[x]) != 1:
            if answers[x][7] == "left":
                v = to_vec(x)
                for a in range(4):
                    lvec[a] += v[a]
                    lvec[a] %= 2
            else:
                v = to_vec(x)
                for a in range(4):
                    rvec[a] += v[a]
                    rvec[a] %= 2
    for a in range(4):
        if rvec[a] != 0:
            break
    else:
        print("right")
        continue
    for a in range(4):
        if lvec[a] != 0:
            break
    else:
        print("left")
        continue
    print("pass")
