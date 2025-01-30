# pcost.py
#
# Exercise 1.27

cost = 0.0

with open('Data/portfolio.csv') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price = float(row[2])
        cost += shares * price

print(f'Total cost {round(cost, 2)}')