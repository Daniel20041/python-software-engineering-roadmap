account_balance = float(input("what's your account balance?"))
risk_percentage = float(input("How much do you want to risk?"))


money_at_risk = account_balance * risk_percentage/100
print(f"You are risking £{money_at_risk: .2f}.")

