# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):
    cost = 0.0

    with open(filename) as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print("Warninng: couldn't parse", row)
            cost += shares * price

    print(f'Total cost {round(cost, 2)}')