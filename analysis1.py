import csv
import matplotlib.pyplot as plt

def read_portfolio(filename):
    portfolio = {}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)
        initialDate=''
        invested_amount=[]
        invested_amount_daily=0

        for row in csv_reader:
            if not row or (row[0].strip()) == "":
                continue  # Skip empty lines or lines with only spaces
            date, name, sector, quantity, price = row
        
            if not date==initialDate:
                initialDate=date
                invested_amount.append(invested_amount_daily)
                invested_amount_daily=0
            
            quantity,price= int(quantity),float(price)
            invested_amount_daily+=quantity*price



            if sector in portfolio:
                portfolio[sector] += quantity
            else:
                portfolio[sector] = quantity
    print(invested_amount)
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