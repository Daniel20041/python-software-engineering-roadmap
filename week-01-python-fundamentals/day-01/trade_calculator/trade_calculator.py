# EXERCISE 5 - FULL TRADING CALCULATOR
#
# Build an interactive trading calculator using only:
# variables, input(), float(), print(), f-strings, +, -, *, /
#
# REQUIREMENTS:
print("---Trading Calculator---")
# 1. Ask the user for:
#    - Trader name
#    - Account balance
#    - Risk percentage
#    - Reward-to-risk ratio
name = input("Enter Trader Name: ")
account_balance = float(input("Enter account balance: "))
risk_percentage = float(input("Enter risk percentage: "))
risk_to_reward_ratio = float(input("Enter risk to reward: "))

print(name,  account_balance, risk_percentage, risk_to_reward_ratio)
#
# 2. Use EURUSD as the trading pair.
trading_pair = "EURUSD"
# 3. Calculate:
#    - Money at risk
#      Formula: account balance * risk percentage / 100
money_risk = account_balance * risk_percentage/ 100
#
#    - Potential profit
#      Formula: money at risk * reward-to-risk ratio
profit = money_risk * risk_to_reward_ratio

#    - Balance after a winning trade
#      Formula: account balance + potential profit
Balance_winningTrade = account_balance + profit

#    - Balance after a losing trade
#      Formula: account balance - money at risk
balance_losingTrade = account_balance - money_risk

#    - Potential percentage return
#      Formula: risk percentage * reward-to-risk ratio
percentage_return = risk_percentage * risk_to_reward_ratio

# 4. Print a clear summary showing:
#    - Trader name
#    - Trading pair
#    - Account balance
#    - Risk percentage
#    - Reward-to-risk ratio
#    - Money at risk
#    - Potential profit
#    - Balance after win
#    - Balance after loss
#    - Potential percentage return
print("---Summary---")
print(f"Trader name: {name}")
print(f"Trading pair: {trading_pair}")
print(f"Account balance: £{account_balance}")
print(f"Risk percentage: {risk_percentage} ")
print(f"Risk to reward ratio: {risk_to_reward_ratio: .2f}")
print(f"Money at risk: £{money_risk: .2f}")
print(f"Potential profit: £{profit: .2f}")
print(f"Balance after win: £{Balance_winningTrade: .2f}")
print(f"Balance after loss: £{balance_losingTrade: .2f}")
print(f"Potential return: {percentage_return: .1f}%")

# 5. Format money values to 2 decimal places.
#
# TEST DATA:
# Name: Daniel
# Account balance: 10000
# Risk percentage: 1
# Reward-to-risk ratio: 7
#
# EXPECTED CALCULATIONS:
# Money at risk: £100.00
# Potential profit: £700.00
# Balance after win: £10700.00
# Balance after loss: £9900.00
# Potential return: 7%
#
# Do not use if statements, loops, functions, or AI-generated code.