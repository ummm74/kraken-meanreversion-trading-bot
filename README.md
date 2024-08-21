# kraken-meanreversion-trading-bot

This project is a Python-based cryptocurrency trading bot designed for mean reversion strategies. The bot trades on a futures demo Kraken exchange using multiple trading pairs. It continuously monitors the market and executes trades based on a predefined mean reversion strategy.

### Features
- Mean Reversion Strategy: The bot implements a mean reversion strategy, which is based on the principle that prices will tend to revert to their historical mean over time. The bot identifies when an asset is overbought or oversold to execute buy/sell orders.
- WebSocket API: Utilizes Kraken's WebSocket API for real-time market data and order execution.
- Multiple Trading Pairs: Supports trading across multiple cryptocurrency pairs.
- Configurable: Allows customization of trading parameters, strategy, and supported pairs.

## Project Structure

```ruby
├── Mean_Strategy.py            # Python script containing the mean reversion strategy
├── README.md                   # Project documentation
├── authkeys.env                # Environment file storing Kraken API keys
├── krkn_main.ipynb             # Jupyter Notebook for running the main bot and testing
├── websocket_api_kraken.py     # Python script handling WebSocket API integration with Kraken
```

## Getting Started

### Prerequisites

- Python 3.8+
- A Kraken account with API keys (read and trade permissions enabled)

### Installation

1. Clone the repository:
```ruby
git clone https://github.com/yourusername/kraken-meanreversion-trading-bot.git
cd kraken-meanreversion-trading-bot
```
2. Install dependencies
```ruby
pip install -r requirements.txt
```
3. Set up API keys
Replace the placeholder values in authkeys.env with your Kraken API key and secret.
```ruby
# authkeys.env
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
```

## Usage

1. Configure trading pairs
Open websocket_api_kraken.py go to the method def subscribe_to_ticker(self) and update the "product_ids" attribute to add to the list with additional pairs.
```ruby
   def subscribe_to_ticker(self):
        subscribe_message = {
            "event": "subscribe",
            "feed": "ticker",
            "product_ids": ["PI_XBTUSD"]
        }
```
2. Run the bot
Start bot with this command
```ruby
python krkn_main.py
```
3. Monitoring
The bot will output logs detailing its trading decisions and market analysis. You can stop the bot at any time by stopping the script.

## Troubleshooting
- Connection Issues:
  Ensure your internet connection is stable and that the Kraken API is operational
- Trading Errors:
  Check if your API keys are correct and have sufficient permissions.
- WebSocket Issues:
  The WebSocket connection might drop occasionally; the bot is designed to reconnect automatically.

## Acknowledgments
- [Kraken API Documentation](https://docs.kraken.com/api/)
- [Kraken WebSocket API Documentation](https://docs.kraken.com/websockets/)
