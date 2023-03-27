#Task 2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
totals_per_item = {k:prices[k]*stock[k] for k in stock}
total_sum = sum(prices[k]*stock[k] for k in stock)
print(totals_per_item)
print(total_sum)

