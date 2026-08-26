trader_name = "Daniel"
account_balance = 10000
trading_pair = "EURUSD"
risk_percentage = 1

print(f"Trader: {trader_name}")
print(f"Account: {account_balance}")
print(f"Pair: {trading_pair}")
print(f"Risk: {risk_percentage}%")


Account = 15000
Risk = 0.5
Risk_to_reward= 8

money_at_risk = Account * Risk/100
potential_profit = money_at_risk * Risk_to_reward

print(f"Money at risk £{money_at_risk}")
print(f"Potential profit £{potential_profit}")