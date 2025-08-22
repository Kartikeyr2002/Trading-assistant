import requests
import urllib3

# Disable SSL warnings (for development only)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Replace with your actual Finnhub API key
FINNHUB_API_KEY = "d2k2v29r01qj8a5lq9sgd2k2v29r01qj8a5lq9t0"

def fetch_market_data(symbol):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        # Disable SSL verification
        response = requests.get(url, verify=False)
        response.raise_for_status()
        data = response.json()

        return {
            "symbol": symbol,
            "current_price": data.get("c"),  # Current price
            "previous_close": data.get("pc"),  # Previous close
            "open": data.get("o"),
            "day_high": data.get("h"),
            "day_low": data.get("l"),
        }
    except requests.exceptions.RequestException as e:
        return {"symbol": symbol, "error": str(e)}
