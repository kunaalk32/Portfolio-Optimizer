# Stock Portfolio Optimizer

This project is my foray into Machine Learning. Using the Sequential Least Squares algorithm in scipy, I maximize the Sharpe Ratio (https://en.wikipedia.org/wiki/Sharpe_ratio) of a given portfolio. This program suggest a new portfolio allocation based off of this new ratio.

## Purpose
This program is not designed for actual use to predict the stock market. It is just my first foray into applying some statistics/data science to finance. The Sharpe Ratio is a very rudimentray metric, and likely won't give you an edge in the market. The analysis also suffers from lookback bias so the results can't be used practically.

## Getting Started

This project uses python 3.6.
To run, simply type: 
```
python optimizer.py
```
