####
# Goal: Optimize The Sharpe Ratio of a given portfolio by reditributing portfolio holdings
####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo

def main():
    # Create a Pandas Dataframe to hold all the data
    # Initialize the dataframe with the dates to be used as data points

    start_date = '2015-1-1'
    end_date = '2017-7-1'
    dates = pd.date_range(start_date, end_date)
    frame = pd.DataFrame(index=dates)

    symbols = ['SPY', 'AAPL', 'GOOG', 'IBM', 'NVDA'] #Stocks in the simulated portfolio; SPY is included as a benchmark for the market
    


if(__name__ == '__main__'):
    main()