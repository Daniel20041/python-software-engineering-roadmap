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
# risk % needs to be stored
# daily loss, trades taken, wheather high impact news is active or not.
# account balance
#
#
# STEPS:
# How would I solve the problem manually?
# i would get all the inputs i needed from the user and then i would work out,
#  what amount is at risk and then define it into a risk classification and label the trade classification accordingly,
# and then lastly i would put the trade status by checking if all rules have been followed and put trade status as either permitted or not permitted.
#
#
# EDGE CASES:
# What boundaries are important?
# it's important that the user gives a valid response but we are going to assume all responses are valid for this exercise.
# its also important that we adhear to the constraints and also make sure the correct output is produced.