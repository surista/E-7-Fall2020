# cli.py
#
# Echo the command line arguments
# Usage:
#      % python cli.py one two three
#
# Jeff Parker, June 23, 2018

import sys

# print the command line arguments
print(sys.argv)

# print one command line argument at a time
for w in sys.argv:
    print(w)
