def generate_signal(market_data):
    mean_price = sum(market_data) / len(market_data)
    current_price = market_data[-1]
    
    if current_price < mean_price * 0.95:
        return 'buy'
    elif current_price > mean_price * 1.05:
        return 'sell'
    else:
        return 'hold'

