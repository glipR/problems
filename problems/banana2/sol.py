J, M = list(map(int, input().split()))

total = 0

while True:
    if J > M:
        M, J = J, M
    banana = min(J//2, M//4)
    if banana == 0:
        break
    total += banana
    J -= banana
    M -= 2 * banana

if J > M:
    M, J = J, M
while M >= 2 and J >= 1:
    M -= 2
    J -= 1
    if J > M:
        M, J = J, M
    total += 1

print(total)

