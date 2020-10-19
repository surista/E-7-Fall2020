# contract.py
#
# The Party of the First Part
#
# Usage:
#      % python contract.py
#
# Jeff Parker, June 26 2018


# Illustrate the mapping between parameters ...
# Takes two names, returns a string
def contract(first: str, second: str) -> str:
    return first + ", " + second


# ... and arguments
print(contract('Grouch', 'Chico'))
print(contract(1, 2))
