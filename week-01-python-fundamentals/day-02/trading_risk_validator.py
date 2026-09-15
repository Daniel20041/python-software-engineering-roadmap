# EXERCISE 7 - TRADING RISK VALIDATOR
#
# Goal:
# Build a command-line program that checks whether a proposed trade
# follows a set of risk-management rules.
#
# Inputs:
# - Account balance
# - Risk percentage for the trade
# - Current daily loss percentage
# - Number of trades already taken today
# - Whether high-impact news is active
#
# Trade is permitted only if:
# - Risk <= 1%
# - Daily loss < 3%
# - Trades taken < 5
# - High-impact news is NOT active
#
# Risk classification:
# - Risk <= 0.5%        -> LOW RISK
# - Risk > 0.5% <= 1%  -> NORMAL RISK
# - Risk > 1%           -> HIGH RISK
#
# Required output:
# - Amount at risk
# - Risk classification
# - Trade status
#
# Constraints:
# Use:
# - variables
# - input()
# - int()
# - float()
# - arithmetic
# - comparisons
# - if / elif / else
# - and / or / not
# - print()
# - f-strings
#
# Do not use:
# - loops
# - functions
# - lists
# - dictionaries
# - classes
#
# Before coding, think through:
#
# INPUT:
# What information does the program receive?
# the program receives : 
# -Account balance
# - Risk percentage for the trade
# - Current daily loss percentage
# - Number of trades already taken today
# - Whether high-impact news is active
#
#
# OUTPUT:
# What should the program produce?
# the program should output:
# - Amount at risk
# - Risk classification
# - Trade status
#
#
# RULES:
# What conditions control the program?
# A trade is permitted only if all of these conditions are satisfied:
# Risk per trade is no greater than 1%
# Current daily loss is below 3%
# Fewer than 5 trades have already been taken today
# No high-impact news event is active
# If any one of those rules is broken, the trade must be rejected.
#
#
# DATA:
# What values need to be stored?
# # DATA:
# - account balance
# - risk percentage
# - current daily loss percentage
# - number of trades already taken
# - whether high-impact news is active
# - calculated amount at risk
# - risk classification
# - trade status
#
# STEPS:
# 1) Get and store all required inputs from the user:
#    - account balance
#    - risk percentage
#    - current daily loss percentage
#    - trades already taken
#    - whether high-impact news is active
#
# 2) Calculate the amount of money at risk using the account balance
#    and risk percentage.
#
# 3) Classify the risk percentage:
#    - <= 0.5% = LOW RISK
#    - > 0.5% and <= 1% = NORMAL RISK
#    - > 1% = HIGH RISK
#
# 4) Store the correct risk classification.
#
# 5) Check whether all trade rules have been satisfied:
#    - risk <= 1%
#    - daily loss < 3%
#    - trades taken < 5
#    - no high-impact news
#
# 6) Set the trade status as permitted or not permitted.
#
# 7) Display:
#    - amount at risk
#    - risk classification
#    - trade status
#
# EDGE CASES:
# What boundaries are important?
# it's important that the user gives a valid response but we are going to assume all responses are valid for this exercise.
# its also important that we adhear to the constraints and also make sure the correct output is produced.
# with risk percentage has to be strictly less than or equal to 0.5% to be classed as low risk. anything above like 0.51% is classes normal risk
# with normal risk it has to be greater than 0.5% but also less than or equal to 1% so 0.99% is still normal risk
# high risk is strictly greater than 1% so even 1.00001% would be classed as high risk
# with the trade rules : risk has to be strictly <= 1% hence 0.99% is sill permitted but 1.00001% is not permitted
# daily loss is strictly less than 3% so a daily loss that is 2% is permitted but daily loss of 3% is not permitted
# trades taken has to be strictly less than 5 so 4 trades is permitted but 5 trades or 6 are not permitted trades
# there has to be no high impact news hence the bool has to be false or else the trade will not be permitted.



# 1) Get and store all required inputs from the user
account_balance = float(input("Enter account balance: "))
risk_percentage = float(input("Enter your risk percentage: "))
daily_loss_percentage = float(input("Enter current daily loss: "))
taken_trades = int(input("Enter number of trades taken today: "))
news_response = input("Is high impact news active? Yes or No: ")
valid_response = None
high_impact_news = None


# checking high impact news
if news_response == "yes" or  news_response == "Yes":
    valid_response = True
    high_impact_news = True
   # print("high impact news is true")
elif news_response == "no" or news_response == "No":
    valid_response = True
    high_impact_news = False
   # print("high impact news is false")
else:
    high_impact_news = None
    valid_response = False




if valid_response:


    # 2) Calculate the amount of money at risk using the account balance and risk percentage.
    amount_of_money_at_risk = account_balance * risk_percentage/100

    # 3) Classify the risk percentage: - <= 0.5% = LOW RISK    - > 0.5% and <= 1% = NORMAL RISK  - > 1% = HIGH RISK
    risk_classification = None

    if risk_percentage <= 0.5:

        risk_classification = "low risk"
    elif risk_percentage > 0.5 and risk_percentage <= 1:
        risk_classification = "Normal risk"
    else:
        risk_classification = "High risk"

    # 5) Check whether all trade rules have been satisfied:
    trade_status = None

    if risk_percentage <= 1 and daily_loss_percentage < 3 and taken_trades < 5 and not high_impact_news:
        trade_status = "This trade has been permitted!"
    else:
        trade_status = "This trade has not been permitted!"



    # Display:

    print(f"Amount at risk: £{amount_of_money_at_risk:.2f}")
    print(f"Risk classification: {risk_classification}")
    print(f"Trade status: {trade_status}")
else:
    print(" invalid response. Please enter Yes or No: ")