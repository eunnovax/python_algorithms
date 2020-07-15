# O(n) time, O(n) space complexity
def buy_sell_twice(prices):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)
    #Forward phase. 1st buysell
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    #Backward phase. max profit on second buysell
    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i-1])
    return max_total_profit

# O(n) time, O(1) space complexity
def buy_sell_twice_2(prices):
    if len(prices) == 0:
        return 0
    minPrice = float('inf')
    maxProfitAfterFirstSell = 0
    maxProfitLeftAfterSecondBuy = float('-inf')
    maxProfitAfterSecondSell = 0

    for i, price in enumerate(prices):
        maxProfitAfterFirstSell = max(maxProfitAfterFirstSell, price - minPrice)
        minPrice = min(minPrice, price)
        maxProfitLeftAfterSecondBuy = max(maxProfitLeftAfterSecondBuy, maxProfitAfterFirstSell - price)
        maxProfitAfterSecondSell = max(maxProfitAfterSecondSell, maxProfitLeftAfterSecondBuy + price)
    return maxProfitAfterSecondSell

A = [12,11,13,9,12,8,14,13,15]
print(buy_sell_twice(A))
print(buy_sell_twice_2(A))