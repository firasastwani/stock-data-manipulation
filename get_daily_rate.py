import pandas as pd
import matplotlib.pyplot as plt

def get_daily_return(file_path):
    data = pd.read_csv(file_path)
    daily_returns_formula = (data['Adj Close'] / data['Adj Close'].shift(1)) - 1
    daily_returns_formula.iloc[0] = 0
    data['Daily Return'] = daily_returns_formula * 100
    return data[['Date', 'Daily Return']]

# Load and compute daily returns for AAPL and SPY
aapl_data = get_daily_return('data/GOOG.csv')
spy_data = get_daily_return('data/GOOG.csv')

# Plotting ----
plt.figure(figsize=(12, 6))
plt.plot(aapl_data['Date'], aapl_data['Daily Return'], label='AAPL Daily Return', color='blue')
plt.plot(spy_data['Date'], spy_data['Daily Return'], label='SPY Daily Return', color='green')

# Add gridlines
plt.grid(True, which='both', linestyle=':', color='lightgray')  # Light gray, dotted gridlines

# Formatting the plot
plt.xlabel('Date')
plt.ylabel('Daily Return (%)')
plt.title('Daily Returns of AAPL vs SPY')
plt.legend()
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.tight_layout()

# Adjust the x-axis to handle overlapping date labels (and ticks) --> (gca() get current axis)
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(20))  # Increase the number of x-axis gridlines
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(10))  # Increase the number of y-axis gridlines

plt.show()