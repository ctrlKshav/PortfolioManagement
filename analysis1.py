import csv
import matplotlib.pyplot as plt

def read_portfolio(filename):
    sectors = {}
    invested_amount={}
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)
        initialDate=''
        invested_amount_daily=0

        for row in csv_reader:
            if not row or (row[0].strip()) == "":
                continue  # Skip empty lines or lines with only spaces
            date, name, sector, quantity, price = row
        
            if not date==initialDate:
                invested_amount[initialDate]=invested_amount_daily
                initialDate=date    
                invested_amount_daily=0
            
            quantity,price= int(quantity),float(price)
            invested_amount_daily+=quantity*price



            if sector in sectors:
                sectors[sector] += quantity
            else:
                sectors[sector] = quantity
        else:
            invested_amount.pop('')
            invested_amount[initialDate]=invested_amount_daily
            
    # print(invested_amount)
    return (sectors,invested_amount)

def plot_sector_percentage_pie(sectors, selected_sector):
    labels = list(sectors.keys())
    sizes = [sectors[sector] for sector in labels]
    explode = [0.1 if sector == selected_sector else 0 for sector in labels]
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title(f'Sector Percentage in Portfolio (Selected Sector: {selected_sector})')
    plt.show()
    
def plot_investment_amount(invested_amount):
    data=invested_amount    
