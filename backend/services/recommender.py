from backend.utils.fetch_data import fetch_market_data

def generate_trade_recommendations():
    symbols = ["AAPL", "TSLA", "MSFT"]  # Sample stocks
    recommendations = []

    for symbol in symbols:
        data = fetch_market_data(symbol)

        if "error" in data:
            recommendations.append({
                "symbol": symbol,
                "action": "Error",
                "reason": data["error"]
            })
            continue

        # Simple logic: Buy if current price > previous close and volume is high
        if data["current_price"] and data["previous_close"]:
            price_change = data["current_price"] - data["previous_close"]
            volume = data.get("volume", 0)

            if price_change > 0 and volume > 1000000:
                action = "Buy"
                reason = "Price is rising with high volume."
            elif price_change < 0:
                action = "Sell"
                reason = "Price is dropping."
            else:
                action = "Hold"
                reason = "Stable price movement."

            recommendations.append({
                "symbol": symbol,
                "action": action,
                "reason": reason,
                "current_price": data["current_price"],
                "previous_close": data["previous_close"],
                "volume": volume
            })

    return recommendations
