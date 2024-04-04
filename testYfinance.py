import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Download data for a specific stock from Yahoo Finance
# stock_data = yf.download('BTC-USD', start='2021-01-01', end='2023-12-31')
stock_data = yf.Ticker('aapl')
print(type(stock_data))
print('hi')
print(stock_data)
# print(stock_data.head())

# Extract the closing prices from the downloaded data

# closing_prices=stock_data['Close']
closing_prices = stock_data.history( start="2020-06-02", end="2020-10-07",interval="1mo")
print(type(closing_prices))
print(closing_prices)
print(closing_prices.loc['2020-10-01','Close'])

# # Compute basic statistics using NumPy
# mean_price = np.mean(closing_prices)
# median_price = np.median(closing_prices)
# std_dev = np.std(closing_prices)
# max_price = np.max(closing_prices)
# min_price = np.min(closing_prices)

# # Print the computed statistics
# print("Mean Price:", mean_price)
# print("Median Price:", median_price)
# print("Standard Deviation:", std_dev)
# print("Max Price:", max_price)
# print("Min Price:", min_price)

# # Plot the closing prices
# plt.figure(figsize=(10, 6))
# plt.plot(closing_prices.index, closing_prices, label='Bitcoin Closing Prices', color='blue')

# # Add title and labels
# plt.title('Bitcoin Closing Prices (2022)')
# plt.xlabel('Date')
# plt.ylabel('Price')

# # Rotate x-axis labels for better readability
# plt.xticks(rotation=45)

# # Add a legend
# plt.legend()

# # Show plot
# plt.tight_layout()
# plt.show()