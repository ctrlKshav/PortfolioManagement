# import numpy as np
import matplotlib.pyplot as plt
# Example asset allocation data (percentages)
asset_allocation = {
    'Stocks': 60,
    'Bonds': 30,
    'Cash': 10
}

# Extract labels and allocation percentages
labels = asset_allocation.keys()
sizes = asset_allocation.values()

# Plot pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Asset Allocation')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

# # Define stock prices for two assets (example data)
# stock_price_asset1 = np.array([100, 105, 110, 115, 120])  # Example prices for Asset 1
# stock_price_asset2 = np.array([150, 155, 160, 165, 170])  # Example prices for Asset 2

# # Calculate daily returns for each asset
# returns_asset1 = np.diff(stock_price_asset1) / stock_price_asset1[:-1]
# returns_asset2 = np.diff(stock_price_asset2) / stock_price_asset2[:-1]

# # Calculate cumulative returns for each asset
# cumulative_returns_asset1 = np.cumprod(1 + returns_asset1) - 1
# cumulative_returns_asset2 = np.cumprod(1 + returns_asset2) - 1

# # Define time periods (assuming 5 days of data)
# time_periods = np.arange(1, len(stock_price_asset1))

# # Plot cumulative returns for each asset
# plt.figure(figsize=(10, 6))
# plt.plot(time_periods, cumulative_returns_asset1, label='Asset 1', marker='o')
# plt.plot(time_periods, cumulative_returns_asset2, label='Asset 2', marker='s')
# plt.xlabel('Time Period')
# plt.ylabel('Cumulative Return')
# plt.title('Cumulative Returns of Portfolio Assets')
# plt.xticks(time_periods)
# plt.legend()
# plt.grid(True)
# plt.show()
