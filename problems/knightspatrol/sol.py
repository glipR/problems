N_PEOPLE = 7

binary = [0] * N_PEOPLE

for x in range(1 << N_PEOPLE):
    tmp = 0
    for i in range(N_PEOPLE):
        binary[i] = str(int(x & (1 << i) != 0))
        if x & (1 << i) != 0:
            tmp ^= i + 1
    print("".join(binary), end=" ")
    if tmp == 0:
        print('1'*N_PEOPLE)
    else:
        guards = ['0'] * N_PEOPLE
        guards[tmp - 1] = '1'
        print(''.join(guards))   
