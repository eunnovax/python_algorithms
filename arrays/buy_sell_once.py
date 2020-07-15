def buy_sell_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit