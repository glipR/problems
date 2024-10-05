from copy import deepcopy

n_people, n_transactions = list(map(int, input().split()))
balances = {}
people = []

for _ in range(n_people):
    name, balance = input().split()
    balances[name] = int(balance)
    people.append(name)

transactions = []
for _ in range(n_transactions):
    name1, _gives, name2, amount = input().split()
    amount = int(amount)
    transactions.append((name1, name2, amount))

frauds = []
for person in people:
    cur_balance = deepcopy(balances)
    for name1, name2, amount in transactions:
        if name1 == person or name2 == person:
            continue
        cur_balance[name1] -= amount
        cur_balance[name2] += amount
        if cur_balance[name1] < 0:
            break
    else:
        # If we never broke out, this person is the fraudulent one
        frauds.append(person)

if len(frauds) != 1:
    raise ValueError()
print(frauds[0])
