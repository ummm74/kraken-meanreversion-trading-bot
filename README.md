# kraken-meanreversion-trading-bot

This project is a Python-based cryptocurrency trading bot designed for mean reversion strategies. The bot trades on the demo Kraken exchange using multiple trading pairs. It continuously monitors the market and executes trades based on a predefined mean reversion strategy.

Features
- Mean Reversion Strategy: The bot implements a mean reversion strategy, aiming to buy low and sell high based on market conditions.
- WebSocket API: Utilizes Kraken's WebSocket API for real-time market data and order execution.
- Multiple Trading Pairs: Supports trading across multiple cryptocurrency pairs.
- Configurable: Allows customization of trading parameters, strategy, and supported pairs.

Project Structure

```ruby
├── Mean_Strategy.ipynb         # Jupyter Notebook for testing and developing the strategy
├── Mean_Strategy.py            # Python script containing the mean reversion strategy
├── README.md                   # Project documentation
├── authkeys.env                # Environment file storing Kraken API keys
├── krkn_main.ipynb             # Jupyter Notebook for running the main bot and testing
├── websocket_api_kraken.ipynb  # Jupyter Notebook for testing WebSocket API integration
├── websocket_api_kraken.py     # Python script handling WebSocket API integration with Kraken
```

Getting Started

Prerequisites

- Python 3.8+
- A Kraken account with API keys (read and trade permissions enabled)

Installation

Clone the repository:
```ruby
git clone https://github.com/yourusername/kraken-meanreversion-trading-bot.git
cd kraken-meanreversion-trading-bot
```
