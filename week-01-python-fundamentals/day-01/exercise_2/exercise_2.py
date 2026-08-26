Account_balance = 12500
Risk = 0.75
Reward_to_risk_ratio = 6

money_at_risk = Account_balance * Risk / 100
potential_profit = money_at_risk * Reward_to_risk_ratio
balance_after_winning = Account_balance + potential_profit
balance_after_losing = Account_balance - money_at_risk


print("balance: ", Account_balance)
print("money at risk: ", money_at_risk)
print("profit: ",potential_profit)
print("losing balance:", balance_after_losing)
print("winning balance:",balance_after_winning)