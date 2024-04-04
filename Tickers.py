import yfinance as yf

class Stock:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.ticker = yf.Ticker(ticker_symbol)
        self.sector = self.info.get('sector', 'N/A')
        self.price_history = self.get_price_history()
   
    def get_price_history(self):
        # Fetch price history from Yahoo Finance
        data = self.ticker.history(period='max')
        return data['Close']  # Only return the closing prices
    # def __str__(self):
    #     return f"Stock: {self.symbol}, Quantity: {self.quantity}, Purchase Price: {self.purchase_price}, Current Price: {self.current_price}"


# List of 10 popular stock tickers
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL','META', 'TSLA', 'NVDA', 'NFLX', 'JPM', 'V']

price_history={}

# Iterate through each ticker
for ticker_symbol in tickers:
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    data = ticker.history(start="2020-06-02", end="2020-10-07")
    
    # Store the price history DataFrame in the dictionary
    price_history[ticker_symbol] = data
    
    # Get stock info

    stock_info = ticker.info
    print(type(stock_info))
    
    # Extract relevant information
    company_name = stock_info['longName']
    company_sector = stock_info['sector']
    market_cap = stock_info['marketCap']
    
    # Print the information
    print(f"Ticker: {ticker_symbol}")
    print(f"Company Name: {company_name}")
    print(f"Sector: {company_sector}")
    print(f"Market Cap: {market_cap}\n")

    print()
# print(price_history)
# print(type(price_history['AAPL']))
print(price_history['AAPL']['Open'])