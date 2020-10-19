# greet2.py
#
# Greet someone
#
# Usage:
#      % python greet2.py
#
# Jeff Parker, June 2018


# Return a greeting
# Takes a name, returns a string
def greet(name: str) -> str:
    return "Hello, " + name


s = greet('Sam')
print(type(s))
print(s)
