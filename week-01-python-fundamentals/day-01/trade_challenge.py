# TRADE PERFORMANCE CALCULATOR
# Problem
# -------
# Build a command-line program that calculates the performance of a
# sequence of trades using a fixed-risk trading strategy.
#
# Requirements
# ------------
# The program must accept:
#
# - Starting account balance
# - Total number of trades
# - Number of winning trades
# - Number of losing trades
# - Risk percentage per trade
# - Reward-to-risk ratio
#
# Assume:
#
# - Risk is always calculated from the original starting balance.
# - The account does not compound between trades.
# - All losing trades lose the full amount at risk.
# - All winning trades achieve the full reward-to-risk target.
# - Inputs can be assumed to be valid.
#
# The program must calculate and display:
#
# - Amount risked per trade
# - Profit from one winning trade
# - Total losses
# - Total gross profit from winning trades
# - Net profit/loss
# - Final account balance
# - Percentage return
#
# Monetary values must be displayed to 2 decimal places.
#
# Test Case
# ---------
# Starting balance: 10000
# Total trades: 10
# Wins: 4
# Losses: 6
# Risk: 1%
# Reward-to-risk ratio: 7
#
# Constraints
# -----------
# Use only concepts covered so far:
# - Variables
# - input()
# - Numeric type conversion
# - Arithmetic
# - print()
# - f-strings
#
# Do not use:
# - if / elif / else
# - loops
# - functions
# - lists or dictionaries
#
# Do not hard-code any calculated result.


startingBalance = float(input("Please enter starting balance: "))
totalTrades = float(input("Please enter your total trades: "))
totalWinsTrades = float(input("Please enter your total wins: "))
totalLossesTrades = float(input("Please enter your total losses: "))
risk =  float(input("Please enter your risk: "))
riskToReward = float(input("Please enter your risk to reward: "))


amountRiskPerTrade = startingBalance * risk/100
profitFromOneWinningTrade = amountRiskPerTrade * riskToReward
totalLosses = profitFromOneWinningTrade * totalLossesTrades
totalGrossProfitFromWinningTrades = profitFromOneWinningTrade * totalWinsTrades
netProfit_Loss = totalGrossProfitFromWinningTrades - totalLosses
finalBalance = startingBalance + netProfit_Loss
percentageRerturn = ((finalBalance - startingBalance)/startingBalance) * 100 

# The program must calculate and display:
#
# - Amount risked per trade
# - Profit from one winning trade
# - Total losses
# - Total gross profit from winning trades
# - Net profit/loss
# - Final account balance
# - Percentage return
#
# Monetary values must be displayed to 2 decimal places.


