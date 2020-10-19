# system.py
#
# Explore variables the system knows
# Usage:
#      % python system.py arguments
#
# Jeff Parker, June 2013

import sys

print("Platform: ",  sys.platform)
print()

print("Arguments:", sys.argv)
print()

print("Path:")
# Print each component in the path
for w in sys.path:
    print(w)
