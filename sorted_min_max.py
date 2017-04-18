# min, max and sorted example to perform

stocks= {
    'YAHOO':38.90,
    'GOOGLE': 340.78,
    'APPLE': 130.5,
    'DISNEY': 110.7,
    'NETFLIX': 140.56
}

print(list(zip(stocks.values(), stocks.keys())))

print(min(list(zip(stocks.values(), stocks.keys()))))

print(max(list(zip(stocks.values(), stocks.keys()))))

print(sorted(list(zip(stocks.values(), stocks.keys()))))