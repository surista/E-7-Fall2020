# which.py
#
# Where is a command defined? 
# Usage:
#      % python which.py command 
#
# Jeff Parker, 2018

import sys
import os

# Is the command in this directory?
def traverse(dir, target):
    try:
        # Loop over all files in this directory
        for w in os.listdir(dir):
            # Is it a match?
            if (target == w):
                return os.path.join(dir, w)
    except:
        return None

    return None

# Get the system path, and traverse each element in turn
def which(target):
    res = os.environ["PATH"]
    path = res.split(':')
    # Look at each element
    for w in path:
        # Is the target there?
        res = traverse(w, target)
        if (res):
            return res

    return "Could not find " + target

if (len(sys.argv) == 1):
    print("Usage: python which.py <command>")
else:
    print(which(sys.argv[1]))

