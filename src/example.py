#######################################################
## ------------------------------------------------- ##
## LIBF Fintech Society - Robofunds Competition 2024 ##
## ------------------------------------------------- ##
#######################################################
##  -----------------------------------------------  ##
##  This is the Example file, this file will not be  ##
##  tested.                                          ##
##                                                   ##
##  This file is to show how to use backtesting.py.  ##
##  -----------------------------------------------  ##
#######################################################

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf
import pandas as pd


# This function will be used to generate indicators
def simple_moving_average(data, window):
    # Return a series of data using the given values
    return pd.Series(data).rolling(window).mean()


# backtesting.py using and object orientated programming style to create strategies
class strategy(Strategy):
    # Optimizable parameters
    short_term_window = 10
    long_term_window = 20

    def init(self):
        # Init is responsible for pre computation of indicators
        close = self.data["Adj Close"]

        # Define indicators by passing in the function and its arguements
        self.short_term_window = self.I(simple_moving_average, close, self.short_term_window)
        self.long_term_window = self.I(simple_moving_average, close, self.long_term_window)


    def next(self):
        # Define logic used to place orders

        # If the two windows cross then buy and sell when they cross again
        if crossover(self.short_term_window, self.long_term_window):
            self.buy()

        elif crossover(self.long_term_window, self.short_term_window):
            self.position.close()


if __name__ == "__main__":
    # This if statement is required, all code to run and test the function must be located under here
    # It is also good practice to move the code below into it's own function but not necessary

    # Load data that stored locally and use pd.read_excel() or pd.read_csv() etc.
    # for this example I will just pull 2 years of prices ending a year ago from yahoo finance based on the current date
    data = yf.download("MSFT",start=datetime.date.today() - relativedelta(years=3), end=datetime.date.today() )

    # Give Backtesting.py it's data and strategy 
    bt = Backtest(data, strategy)

    # Run strategy, print or save results here
    results_1 = bt.run()
    print("-"*100)
    print("Strategy Un-optimised")
    print("")
    print(results_1)
    print("-"*100)

    # Optimisation of parameters

    # Constraint limits the variables
    def optimize_constraint(parameters):
        return parameters["long_term_window"] > parameters["short_term_window"]
    
    # Optimiser maximises the output of this function
    def optimize_function(series):
        if series["# Trades"] < 10:
            # Reject strategies which dont trade enough as this leads to overfitting
            return -float("inf")
        
        else:
            return (series["Equity Final [$]"]) / (series["Exposure Time [%]"] * (1+series["Volatility (Ann.) [%]"]))

    # Finally, optimise. Give the range of values which the strategy can tweak.
    results_2 = bt.optimize(maximize=optimize_function,short_term_window=range(0,60,3), long_term_window=range(0,60,5),constraint=optimize_constraint)
    
    print("-"*100)
    print("Strategy optimised")
    print("")
    print(results_2)
    print("-"*100)

    #plot graph
    bt.plot()

    # Access specific data about the backtest like a pandas Dataframe or dictionary
    print(f"{results_1['Equity Final [$]']} versus {results_2['Equity Final [$]']}")

    # To make a strategy viable to implement in real life it needs to be tested wether the risk adjusted return is significant or not.
