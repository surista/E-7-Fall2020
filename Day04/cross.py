# cross.py
#
# Read the words in a file and look for a match
# Usage:
#      % python cross.py words.txt
#
# Jeff Parker	March 2018

import sys

if (len(sys.argv) != 2):
    print("Usage: python cross.py <words.txt>")
else:
    filename = sys.argv[1]

    with open(filename, 'r') as words:
        for line in words:
            if (len(line) == 4) and (line[-1] == 't'):
                print(line)

