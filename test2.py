import mysql.connector
from datetime import datetime
import hashlib
import matplotlib.pyplot as plt
class RealEstate:
    def _init_(self, id, name, location, purchase_price, current_value, rental_income):
        self.id = id
        self.name = name
        self.location = location
        self.purchase_price = purchase_price
        self.current_value = current_value
        self.rental_income = rental_income

    def update_value(self, new_value):
        self.current_value = new_value

    def calculate_return(self):
        return (self.current_value - self.purchase_price) / self.purchase_price

    def calculate_total_return(self):
        return self.calculate_return() + (self.rental_income / self.purchase_price)

    def calculate_monthly_return(self):
        today = datetime.today()
        days_in_month = today.day
        monthly_rental_income = (self.rental_income) * (days_in_month / 30)
        return ((self.current_value - self.purchase_price) / self.purchase_price) + ((monthly_rental_income / self.purchase_price))


    def calculate_yearly_return(self):
        return (self.current_value - self.purchase_price) / self.purchase_price + (self.rental_income * 12 / self.purchase_price)

class RealEstatePortfolio:
    def _init_(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="devarshi"
        )
        self.cursor = self.db_connection.cursor()

    def add_property(self, property):
        sql_query = "INSERT INTO real_estate (name, location, purchase_price, current_value, rental_income, return_per_month, return_per_year) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        monthly_return = property.calculate_monthly_return()
        yearly_return = property.calculate_yearly_return()
        property_data = (property.name, property.location, property.purchase_price, property.current_value, property.rental_income, monthly_return, yearly_return)
        self.cursor.execute(sql_query, property_data)
        self.db_connection.commit()

    def remove_property(self, property_id):
        sql_query = "DELETE FROM real_estate WHERE id = %s"
        property_id = (property_id,)
        self.cursor.execute(sql_query, property_id)
        self.db_connection.commit()

    def update_property_value(self, property_id, new_value):
        sql_query = "UPDATE real_estate SET current_value = %s WHERE id = %s"
        property_data = (new_value, property_id)
        self.cursor.execute(sql_query, property_data)
        self.db_connection.commit()

    def generate_report(self):
        sql_query = "SELECT * FROM real_estate"
        self.cursor.execute(sql_query)
        properties = self.cursor.fetchall()

        total_return = 0
        for prop in properties:
            property_object = RealEstate(prop[0], prop[1], prop[2], prop[3], prop[4], prop[5])
            monthly_return = property_object.calculate_monthly_return()
            yearly_return = property_object.calculate_yearly_return()
            total_return += property_object.calculate_total_return()
            print(f"Property: {property_object.name}, Location: {property_object.location}, Total Return: {property_object.calculate_total_return()}, Monthly Return: {monthly_return}, Yearly Return: {yearly_return}")
            # Update return_per_month and return_per_year in the database
            sql_query_update = "UPDATE real_estate SET return_per_month = %s, return_per_year = %s WHERE id = %s"
            return_data = (monthly_return, yearly_return, prop[0])
            self.cursor.execute(sql_query_update, return_data)
            self.db_connection.commit()
        print(f"Total Portfolio Return: {total_return}")
        
    def generate_report_save(self, filename):
        sql_query = "SELECT * FROM real_estate"
        self.cursor.execute(sql_query)
        properties = self.cursor.fetchall()

        with open(filename, 'w') as file:
            file.write("Name, Location, Purchase Price, Current Value, Rental Income, Return per Month, Return per Year\n")
            for prop in properties:
                file.write(f"{prop[1]}, {prop[2]}, {prop[3]}, {prop[4]}, {prop[5]}, {prop[6]}, {prop[7]}\n")
        print(f"Report saved to {filename}.")


    def _del_(self):
        self.cursor.close()
        self.db_connection.close()

class Stock:
    def _init_(self, id, symbol, purchase_price, current_price, quantity):
        self.id = id
        self.symbol = symbol
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.quantity = quantity

    def update_price(self, new_price):
        self.current_price = new_price

    def calculate_return(self):
        return (self.current_price - self.purchase_price) * self.quantity

class StockPortfolio:
    def _init_(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="devarshi"
        )
        self.cursor = self.db_connection.cursor()

    def add_stock(self, stock):
        sql_query = "INSERT INTO stocks (symbol, purchase_price, current_price, quantity) VALUES (%s, %s, %s, %s)"
        stock_data = (stock.symbol, stock.purchase_price, stock.current_price, stock.quantity)
        self.cursor.execute(sql_query, stock_data)
        self.db_connection.commit()

    def remove_stock(self, stock_id):
        sql_query = "DELETE FROM stocks WHERE id = %s"
        stock_id = (stock_id,)
        self.cursor.execute(sql_query, stock_id)
        self.db_connection.commit()

    def update_stock_price(self, stock_id, new_price):
        sql_query = "UPDATE stocks SET current_price = %s WHERE id = %s"
        stock_data = (new_price, stock_id)
        self.cursor.execute(sql_query, stock_data)
        self.db_connection.commit()

    def generate_report(self):
        sql_query = "SELECT * FROM stocks"
        self.cursor.execute(sql_query)
        stocks = self.cursor.fetchall()

        total_return = 0
        for stock_data in stocks:
            stock_object = Stock(stock_data[0], stock_data[1], stock_data[2], stock_data[3], stock_data[4])
            total_return += stock_object.calculate_return()
            print(f"Stock: {stock_object.symbol}, Quantity: {stock_object.quantity}, Total Return: {stock_object.calculate_return()}")
        print(f"Total Portfolio Return: {total_return}")

    def close_connection(self):
        self.cursor.close()
        self.db_connection.close()

class User:
    def _init_(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()

class Database:
    def _init_(self):
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ksv"
        )
        self.cursor = self.db_connection.cursor()

    def create_tables(self):
        self.cursor.execute("USE devarshi")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                username VARCHAR(255) UNIQUE,
                                password VARCHAR(64)
                            )""")
        self.db_connection.commit()

    def insert_user(self, user):
        self.cursor.execute("USE devarshi")
        sql_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        user_data = (user.username, user.password)
        self.cursor.execute(sql_query, user_data)
        self.db_connection.commit()

    def verify_user(self, username, password):
        self.cursor.execute("USE devarshi")
        sql_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute(sql_query, (username, hashed_password))
        user = self.cursor.fetchone()
        return user is not None

    def close_connection(self):
        self.cursor.close()
        self.db_connection.close()

if __name__ == "_main_":
    database = Database()
    database.create_tables()

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if database.verify_user(username, password):
                print("Login successful!")
                real_estate_portfolio = RealEstatePortfolio()
                stock_portfolio = StockPortfolio()

                while True:
                    print("1. Add Real Estate Property")
                    print("2. Update Real Estate Property Value")
                    print("3. Remove Real Estate Property")
                    print("4. Generate Real Estate Portfolio Report")
                    print("5. Save Real Estate Portfolio Report")
                    print("6. Add Stock")
                    print("7. Update Stock Price")
                    print("8. Remove Stock")
                    print("9. Generate Stock Portfolio Report")
                    print("10. Logout")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        name = input("Enter property name: ")
                        location = input("Enter property location: ")
                        purchase_price = float(input("Enter purchase price: "))
                        current_value = float(input("Enter current value: "))
                        rental_income = float(input("Enter rental income: "))
                        property = RealEstate(None, name, location, purchase_price, current_value, rental_income)
                        real_estate_portfolio.add_property(property)

                    elif choice == "2":
                        property_id = int(input("Enter property ID: "))
                        new_value = float(input("Enter new value: "))
                        real_estate_portfolio.update_property_value(property_id, new_value)

                    elif choice == "3":
                        property_id = int(input("Enter property ID: "))
                        real_estate_portfolio.remove_property(property_id)

                    elif choice == "4":
                        real_estate_portfolio.generate_report()
                    elif choice == "5":
                        filename = input("Enter filename to save the report: ")
                        real_estate_portfolio.generate_report_save(filename)

                    elif choice == "6":
                        symbol = input("Enter stock symbol: ")
                        purchase_price = float(input("Enter purchase price: "))
                        current_price = float(input("Enter current price: "))
                        quantity = int(input("Enter quantity: "))
                        stock = Stock(None, symbol, purchase_price, current_price, quantity)
                        stock_portfolio.add_stock(stock)

                    elif choice == "7":
                        stock_id = int(input("Enter stock ID: "))
                        new_price = float(input("Enter new price: "))
                        stock_portfolio.update_stock_price(stock_id, new_price)

                    elif choice == "8":
                        stock_id = int(input("Enter stock ID: "))
                        stock_portfolio.remove_stock(stock_id)

                    elif choice == "9":
                        stock_portfolio.generate_report()

                    elif choice == "10":
                        real_estate_portfolio.close_connection()
                        stock_portfolio.close_connection()
                        print("Logged out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")
                break
            else:
                print("Invalid username or password. Please try again.")

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")
            if password == confirm_password:
                user = User(username, password)
                database.insert_user(user)
                database.verify_user(username, password)
                print("Registration successful! Please login.")
            else:
                print("Passwords do not match. Please try again.")

        elif choice == "3":
            database.close_connection()
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")