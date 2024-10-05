import random
import string

names = ["".join(random.choice(string.ascii_lowercase)for _ in range(10)) for _ in range(50)]
balances = [random.randint(0, pow(10, 7)) for _ in range(50)]
balance_map = {
    name: balance
    for name, balance in zip(names, balances)
}

fraud = names[13]

untampered_transactions = []
for _ in range(450):
    while True:
        rd_name = random.choice(names)
        if rd_name == fraud:
            continue
        if balance_map[rd_name] == 0:
            continue
        break
    while True:
        rd_name_2 = random.choice(names)
        if rd_name_2 == fraud:
            continue
        break
    amount = random.randint(1, balance_map[rd_name])
    untampered_transactions.append((rd_name, rd_name_2, amount))
    balance_map[rd_name]   -= amount
    balance_map[rd_name_2] += amount

non_fraud_names = [name for name in names if name != fraud]

fraud_transactions = [
    (random.choice(non_fraud_names), fraud, random.randint(10**7//3, 10**7))
    for _ in range(50)
]

for transaction in fraud_transactions:
    untampered_transactions.insert(random.randint(0, len(untampered_transactions)), transaction)

print(50, len(untampered_transactions))
for name, balance in zip(names, balances):
    print(name, balance)
for name1, name2, amount in untampered_transactions:
    print(name1, "gives", name2, amount)

