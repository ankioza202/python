import heapq

grades=[34, 67, 45, 35, 67, 60]
print(heapq.nlargest(3,grades))


stocks =[
    {'stock_name':'AAPL','price':140},
    {'stock_name':'DIS','price':129},
    {'stock_name':'GOOGLE','price':600},
    {'stock_name':'MSFT','price':54},
    {'stock_name':'AAPL','price':140},
    {'stock_name':'NETFLIX','price':144}

]

print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']))

# Dictionary calculation and find min value

food = {
    'rice': 400,
    'veg': 50,
    'egg': 10,
    'milk': 4,
    'meat': 500
}

min_food_price = min(zip(food.values(), food.keys()))
print(min_food_price)