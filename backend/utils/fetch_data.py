# Fetches real-time market data using open-source APIs like Yahoo Finance.
import requests

def fetch_market_data(symbol):
    # Example using Yahoo Finance API
    url = f"https://query1.finance.yahoo.com/v7/finance/quote?symbols={symbol}"
    response = requests.get(url)
    return response.json()

