import csv
import os
import datetime
import yfinance as yf
import pandas as pd

class Stock:
    def __init__(self, symbol,sector,price):
        self.symbol = symbol  
        self.sector = sector
        self.price=price
        self.ticker=Tickers.tickers[symbol]
        self.price_history=self.ticker.history(period='max')
   
    def update_price(self,date):
        self.price=self.price_history.loc[date,'Close']

    def  __str__(self):
        return f"\nStock : {self.symbol}\nSector : {self.sector}\n Price: {self.price}\n "

class Tickers:
    # List of 10 popular stock tickers

    def __init__(self) -> None:
        self.price=0
    ticker_symbols = ['AAPL', 'GOOG','MSFT', 'AMZN','META', 'TSLA', 'NVDA', 'NFLX', 'JPM', 'V']
    tickers={}
    price_history={}
    # Iterate through each ticker
    for ticker_symbol in ticker_symbols:
        # Create a Ticker object
        ticker = yf.Ticker(ticker_symbol)
        tickers[ticker_symbol]=ticker

        # data = ticker.history(start="2020-06-02", end="2020-10-07")
        
        # Store the price history DataFrame in the dictionary
        # price_history[ticker_symbol] = data
        
        # Get stock info

        # stock_info = ticker.info
        # print(type(stock_info))
        
        # # Extract relevant information
        # company_name = stock_info['longName']
        # company_sector = stock_info['sector']
        # market_cap = stock_info['marketCap']

class Portfolio:
    def __init__(self, portfolio_csv="portfolio.csv", transactions_csv="transactions.csv"):
        self.balance=0.0
        self.net_profit=0.0
        self.portfolio_csv = portfolio_csv
        self.transactions_csv = transactions_csv
        self.portfolio_data = []

        # Create portfolio CSV file if it doesn't exist
        if not os.path.exists(portfolio_csv):
            with open(portfolio_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Date","Symbol","Sector","Quantity","BuyingPrice"])

        # Create transactions CSV file if it doesn't exist
        if not os.path.exists(transactions_csv):
            with open(transactions_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Action","Date", "Symbol", "Quantity", "BuyingPrice"])


    def check_balance(self):
        """
        Check the current balance of the portfolio.
        """
        return self.balance
    
    def deposit_balance(self, amount):
        """
        Deposit funds into the portfolio balance.
        """
        self.balance += amount

    def withdraw_funds(self, amount):
        """
        Withdraw funds from the portfolio balance.
        """
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount

   
    def update_stock_price(self, symbol, current_price):
        updated_rows = []
        with open(self.portfolio_csv, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == symbol:
                    row[3] = current_price
                updated_rows.append(row)

        with open(self.portfolio_csv, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)

    def log_transaction(self,action,date, stock,quantity):
        print('test1')
        print(stock)
        print(type(stock))
        with open(self.transactions_csv, 'a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([action,date, stock.symbol, quantity, stock.price])


    def buy_stock(self, date, stock,quantity):
        total_cost = stock.price * quantity
        if total_cost > self.balance:
            print("Insufficient balance to buy this stock.")
            return
        
        with open(self.portfolio_csv, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([date, stock.symbol, stock.sector, quantity, stock.price])
        self.log_transaction("Buy",date, stock, quantity, )
        self.balance -= total_cost

    def sell_stock(self, date, stock, quantity):
        total_cost = stock.price*quantity
        
        available_quantity = 0
        flag=False
        with open(self.portfolio_csv, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] == stock.symbol:
                    available_quantity = int(row[3])
                    flag=True
                    break
        if not flag:
            print("Stock not in your portfolio ")
            return
        if quantity > available_quantity:
            print("Insufficient shares to sell.")
            return

        # Log the sell transaction
        self.log_transaction('Sell',date,stock,quantity)

        self.balance+=total_cost

        # Update portfolio CSV by removing the sold stock
        temp_csv = self.portfolio_csv + ".temp"
        with open(self.portfolio_csv, 'r', newline='') as file_in, \
                open(temp_csv, 'w', newline='') as file_out:
            reader = csv.reader(file_in, delimiter=';')
            writer = csv.writer(file_out, delimiter=';')
            for row in reader:
                if row[1] == stock.symbol:
                    row[3] = str(int(row[3]) - quantity)
                    if int(row[3]) == 0:  # If quantity becomes zero, skip writing the row
                        continue
                writer.writerow(row)

        # Replace the original portfolio CSV with the temporary file
        os.replace(temp_csv, self.portfolio_csv)

    def view_transaction_history(self):
        with open(self.transactions_csv, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)


    def display_portfolio(self):
        with open(self.portfolio_csv, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
aapl=Stock("AAPL", "Technology", 150.0)
goog=Stock("GOOG", "Technology", 200.0)
msft=Stock("MSFT", "Technology", 300.0)
amzn=Stock("AMZN", "Technology", 350.0)
meta=Stock("META", "Retail", 140.0)
tsla=Stock("TSLA", "Automotive", 650.0)
nvda=Stock("NVDA", "Technology", 400.0)
nflx=Stock("NFLX", "Entertainment", 450.0)
jpm=Stock("JPM", "Entertainment", 170.0)
v=Stock("V", "Finance", 120.0)

stockList=[aapl,goog,msft,amzn,meta,tsla,nvda,nflx,jpm,v]


stocks = {
    "AAPL": aapl,
    "GOOG": goog,
    "MSFT": msft,
    "AMZN": amzn,
    "META": meta,
    "TSLA": tsla,
    "NVDA": nvda,
    "NFLX": nflx,
    "JPM": jpm ,
    "V": v
}



# Trial:
#We come here after pyQT(if it is created)

portfolio = Portfolio()
date='2024-12-12'

while True:
        print("What's on your mind?")
        print("1. Check your Account balance")
        print("2. Deposit money to your account")
        print("3. Withdraw money from your account")
        print("4. View Your Portfolio")
        print("5. View Transaction History")
        print("6. Buy some Shares")
        print("7. Sell some Shares")
        # print("8. Check My Profit")
        print("8. View Shares listed on the Stock Exchange")
        print("9. View a specific Stock")
        print("10. Update Prices of Stocks listed on the Exchange")
        print("11. Open Analysis Section")
        print("0. Exit the program")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            print(portfolio.check_balance())
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            portfolio.deposit_balance(amount)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            portfolio.withdraw_funds(amount)
        elif choice == 4:
            portfolio.display_portfolio()
        elif choice == 5:
            portfolio.view_transaction_history()
        elif choice == 6:
            stock_name = input("Enter the name of the stock to buy: ").strip()
            if stock_name not in stocks.keys():
                print('Stock Not Listed on the Exchange')
                break
            quantity = int(input("Enter the quantity to buy: "))
            portfolio.buy_stock(date,stocks[stock_name], quantity)
        elif choice == 7:
            stock_name = input("Enter the name of the stock to sell: ").strip()
            if stock_name not in stocks.keys():
                print('Stock Not Listed on the Exchange')
                break
            quantity = int(input("Enter the quantity to sell: "))
            portfolio.sell_stock(date,stocks[stock_name], quantity)
        # elif choice == 7:
        #     portfolio.calculateProfit()
        elif choice == 8:
            for stock in stocks:
                print(stocks.get(stock))
        elif choice == 9:
            stock_name = input("Enter the name of the stock to view details: ").strip()
            print(stocks[stock_name])
        elif choice == 10:
           for stock in stockList:
               stock.update_price(input("Enter Date"))
        elif choice == 11:
            print("Open Analysis Section")

        elif choice == 0:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    



# # Add a stock to the portfolio
# portfolio.buy_stock('2024-04-02',stocks['TSLA'],5)
# portfolio.buy_stock('2024-04-02',stocks['MSFT'],5)
# portfolio.buy_stock('2024-04-02',stocks['JPM'],5)

# portfolio.sell_stock('2024-04-02',stocks['TSLA'],5)
# portfolio.sell_stock('2024-04-02',stocks['MSFT'],2)

# Display portfolio
# portfolio.display_portfolio()
