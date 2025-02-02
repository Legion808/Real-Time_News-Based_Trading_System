import alpaca_trade_api as tradeapi

API_KEY = "Your-Alpaca-API-Key"
API_SECRET = "Your-Alpaca-Secret-Key"
BASE_URL = "https://paper-api.alpaca.markets"  # Demo uchun Alpaca API

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')


def execute_trade(signal, symbol, quantity):
    try:
        if signal == "Buy":
            order = api.submit_order(
                symbol=symbol,
                qty=quantity,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
        elif signal == "Sell":
            order = api.submit_order(
                symbol=symbol,
                qty=quantity,
                side='sell',
                type='market',
                time_in_force='gtc'
            )
        else:
            return "No trade executed"
        return f"Order submitted: {order.id}"
    except Exception as e:
        return f"Trade execution failed: {e}"
