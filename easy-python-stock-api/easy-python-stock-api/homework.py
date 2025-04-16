import requests
import matplotlib.pyplot as plt
import pandas as pd
from typing import List, Dict, Set
import datetime

# Define the base URL for the API
base_url = 'http://localhost:8000'

# Function to fetch stock data
def get_stock_data(symbol: str) -> List[float]:

    # TODO see the pseudocode below, fill it in:
    # define a URL variable

    # send a HTTP GET to the right endpoint using requests
    # if it's HTTP 200,
        # return the JSON output as a list

    # if it's not HTTP 200,
        # return an empty list

    return [] # TODO: Delete this line as well, and fill the above method in.


# Function to generate a plot of stock prices
def generate_plot(data: List, symbol: str) -> None:
    dates = [datetime.date.today() + datetime.timedelta(days=i) for i in range(-len(data), 0)]
    prices = pd.Series(data, index=dates)

    plt.figure(figsize=(10, 5))
    plt.plot(prices)
    plt.title(f'{symbol} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()

# Function to export a plot to PNG and XLSX files
def export_plot(data, symbol):
    dates = [datetime.date.today() + datetime.timedelta(days=i) for i in range(-len(data), 0)]
    prices = pd.Series(data, index=dates)

    plt.figure(figsize=(10, 5))
    plt.plot(prices)
    plt.title(f'{symbol} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)

    # Save as PNG file
    filename = f'{symbol}_stock_price.png'
    plt.savefig(filename)
    print(f'Plot saved to {filename}')

    # Save as XLSX file
    filename = f'{symbol}_stock_price.xlsx'
    prices.to_excel(filename)
    print(f'Data exported to {filename}')

MY_STOCKS = ['TSLA', 'AAPL', 'PYTHN']

# Main function
def main():
    # Fetch and plot stock data for each symbol
    for symbol in MY_STOCKS:
        stock_series = get_stock_data(symbol)

        if (len(stock_series) == 0):
            print("Hello! You're probably not done.")

        if stock_series:
            generate_plot(stock_series, symbol)
            export_plot(stock_series, symbol)

main()
