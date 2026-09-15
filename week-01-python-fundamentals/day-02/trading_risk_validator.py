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
#
# OUTPUT:
# What should the program produce?
#
# RULES:
# What conditions control the program?
#
# DATA:
# What values need to be stored?
#
# STEPS:
# How would I solve the problem manually?
#
# EDGE CASES:
# What boundaries are important?