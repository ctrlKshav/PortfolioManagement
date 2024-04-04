import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates


class StockAnalyzer:
    def _init_(self):
        pass
    
    def plot_stock_price(self, stock_name):
        try:
            stock_data = yf.download(stock_name, start="2020-01-01", end="2024-01-01")
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['Close'], label=stock_name)
            plt.title('Stock Price History of ' + stock_name)
            plt.xlabel('Date')
            plt.ylabel('Stock Price (USD)')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("Error:", e)
    
    def plot_volume(self, stock_name):
        try:
            stock_data = yf.download(stock_name, start="2020-01-01", end="2024-01-01")
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['Volume'], label=stock_name)
            plt.title('Volume Traded of ' + stock_name)
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("Error:", e)
    
    def plot_returns(self, stock_name):
        try:
            stock_data = yf.download(stock_name, start="2020-01-01", end="2024-01-01")
            daily_returns = stock_data['Adj Close'].pct_change()
            plt.figure(figsize=(10, 6))
            plt.plot(daily_returns, label=stock_name)
            plt.title('Daily Returns of ' + stock_name)
            plt.xlabel('Date')
            plt.ylabel('Daily Returns')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print("Error:", e)
    
    def calculate_volatility(self, stock_name):
        try:
            stock_data = yf.download(stock_name, start="2020-01-01", end="2024-01-01")
            daily_returns = stock_data['Adj Close'].pct_change()
            volatility = np.std(daily_returns)
            return volatility
        except Exception as e:
            print("Error:", e)

if __name__ == "_main_":
    analyzer = StockAnalyzer()
    stock_name = input("Enter the name of the stock (Ticker Symbol): ").upper()
    print("Volatility of", stock_name + ":", analyzer.calculate_volatility(stock_name))
    analyzer.plot_stock_price(stock_name)
    analyzer.plot_volume(stock_name)
    analyzer.plot_returns(stock_name)