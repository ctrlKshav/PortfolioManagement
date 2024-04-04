import csv
import matplotlib.pyplot as plt

def read_portfolio(filename):
    portfolio = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for row in csv_reader:
            date, name, sector, quantity, price = row
            quantity = int(quantity)
            if sector in portfolio:
                portfolio[sector] += quantity
            else:
                portfolio[sector] = quantity
    return portfolio

def plot_sector_percentage_pie(portfolio, selected_sector):
    labels = list(portfolio.keys())
    sizes = [portfolio[sector] for sector in labels]
    explode = [0.1 if sector == selected_sector else 0 for sector in labels]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title(f'Sector Percentage in Portfolio (Selected Sector: {selected_sector})')
    plt.show()
    
portfolio = read_portfolio('portfolio.csv')
selected_sector = input("Enter the sector you want to analyze: ").capitalize()
plot_sector_percentage_pie(portfolio, selected_sector)