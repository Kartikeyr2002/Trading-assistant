
import yfinance as yf

# List of stock tickers
tickers = ["AAPL", "MSFT", "TSLA"]

# Download and save historical data
for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    df = yf.download(ticker, period="1y", interval="1d")
    df.to_csv(f"{ticker}_historical_data.csv")
    print(f"Saved {ticker}_historical_data.csv")
