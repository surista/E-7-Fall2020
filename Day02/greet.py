# greet.py
#
# Greet someone
#
# Usage:
#      % python greet.py
#
# Jeff Parker, June 2018


# Print a greeting.
# Void function that takes a string
def greet(name: str):
    print("Hello, " + name)


greet('Sam')
greet('Dave')
greet('sam'*2)
print(type(greet('Sam')))
greet(2)
