# Stock Portfolio Optimizer

This project is my foray into Machine Learning. Using the Sequential Least Squares algorithm in scipy, I maximize the Sharpe Ratio (https://en.wikipedia.org/wiki/Sharpe_ratio) of a given portfolio. This program suggest a new portfolio allocation based off of this new ratio.

## Getting Started

This project uses python 3.6.
To run, simply type: 
```
python optimizer.py
```

## Bugs

In cases where the function is not convex, or there are multiple local minima, the optimizer converges to an incorrect result. This will be fixed in future versions.
