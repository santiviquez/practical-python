# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            holding = {'name': row[0],
                       'shares': int(row[1]),
                       'price': float(row[2])}
            portfolio.append(holding)
    
    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        print(rows)
        headers = next(rows)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices


portfolio = read_portfolio('Work/Data/portfolio.csv')
prices = read_prices('Work/Data/prices.csv')

total_cost = 0.0
total_value = 0.0

for stock in portfolio:
    try:
        current_price = prices[stock['name']]
    except KeyError:
        current_price = stock['price']

    total_cost += stock['shares'] * stock['price']
    total_value += stock['shares'] * current_price

print('Portfolio value:', total_value)
print('Gain:', total_value - total_cost)