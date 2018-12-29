####
# Goal: Optimize The Sharpe Ratio of a given portfolio by reditributing portfolio holdings
####
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as spo

symbols = ['SPY', 'AAPL', "GOOG", "IBM", "GS"] #Stocks in the simulated portfolio; SPY is included as a benchmark for the market

def add(frame, symbol):
    temp = pd.read_csv(symbol.lower()+'.csv', usecols=['Date', 'Close'], index_col='Date', na_values=['nan'], parse_dates=True) #read the stock data into the dataframe
    temp = temp.rename(columns={'Close': symbol})
    frame = frame.join(temp)
    return frame


def total(frame, distribution):
    frame *= distribution
    sum = frame.sum(axis=1)
    sum /= sum.iloc[0]
    sum = pd.DataFrame(sum, columns=['Portfolio'])
    return sum

def neg_sharpe(distribution, frame): #since I'm using a minimizer later, I'm multiplying the ratio by negative 1 since a greater ratio is desired
    sum = total(frame, distribution)
    returns = sum.iloc[-1] - sum.iloc[0]
    std = sum.std()
    sharpe = -1*returns/std
    return sharpe



def redistribute(frame, func, guess):
    bounds = tuple((0,1) for x in guess)
    const = ({"type": "eq", "fun": lambda x: sum(x)-1})

    print("Optimization Details:")
    result = spo.minimize(func, guess, args=(frame,), method='SLSQP', options={'disp': True}, bounds=bounds, constraints=const)
    return result.x


def main():
    # Create a Pandas Dataframe to hold all the data
    # Initialize the dataframe with the dates to be used as data points

    start_date = '2015-8-18'
    end_date = '2017-6-30'
    dates = pd.date_range(start_date, end_date)
    frame = pd.DataFrame(index=dates)


    for symbol in symbols:
        frame = add(frame, symbol)
    frame = frame.dropna()

    #create separate dataframes for benchmark and portfolio
    spy_frame = frame['SPY']
    spy_frame = spy_frame/spy_frame.iloc[0] #Normmalize by dividing by first element so only growth is measured
    ax = spy_frame.plot(legend=True)


    del frame['SPY']

    initial = tuple(1/len(frame.columns.values) for x in frame.columns.values)
    # # generate random seed values
    # initial = np.random.normal(0, 3, (len(frame.columns.values)))
    # initial = np.absolute(initial)
    # initial /= np.sum(initial)
    print("Initial Guess: ", initial)
    print("Initial Sharpe: ", -1*neg_sharpe(initial,frame)[0])
    total_frame = total(frame, initial)
    initial_returns = (total_frame.iloc[-1] - total_frame.iloc[0]) * 100
    print("Initial Return: ", initial_returns[0], "%")
    print()


    sum = total(frame, initial)
    sum.plot(ax=ax, legend=True)
    plt.xlabel("Dates")
    plt.ylabel("Growth")
    plt.title('Performance of Even Portfolio Distribution vs. Market')

    #initial state plotted

    coefs = redistribute(frame, neg_sharpe, initial)

    print("Optimal distribution of stocks: ", coefs)
    print()
    portfolio = total(frame, coefs)

    plt.figure()
    spy = spy_frame.plot(legend=True)
    portfolio.plot(ax=spy, legend=True)
    plt.xlabel("Dates")
    plt.ylabel("Growth")
    plt.title("Optimized Portfolio vs. Market")

    print("Final Sharpe: ", -1 * neg_sharpe(coefs, frame)[0])
    total_frame = total(frame, coefs)
    final_returns = (total_frame.iloc[-1] - total_frame.iloc[0]) * 100
    print("Optimal Return: ", final_returns[0], "%")

    plt.show()

if(__name__ == '__main__'):
    main()
