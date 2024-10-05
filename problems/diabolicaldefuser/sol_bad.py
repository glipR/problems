T = int(input())

for _ in range(T):
    answers = [input().split() for __ in range(14)]
    me = input().split()[3]
    answers.append([me])
    answers.sort()
    if len(answers[0]) == 1:
        print("left")
    else:
        print("pass")
