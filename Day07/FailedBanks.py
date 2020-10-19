# Failed Banks.py
#
# Read in information from Excel file saved as CSV
# Usage:
#      % python FailedBanks.py banks.csv
#
# Bank Name,City,ST,CERT,Acquiring Institution,Closing Date,Updated Date
# Fayette County Bank,Saint Elmo,IL,1802,"United Fidelity Bank, fsb",
#    26-May-17,26-Jul-17
#
# Bugs: states without failures don't show up in list of "Best" states
#
# Changes Oct 2020:
#    Create two functions to hold main logic
#    Don't treat first row as valid
#    Use defaultdict rather than LBYL
#    Use a List Comprehension to build result
#    ** Note use of 'reverse' optional parameter in second call to sort() **

import csv      # Read Comma Separated Values (CSV) files
import sys      # Read filename from command line
from collections import defaultdict

from typing import Dict

def read_dict(filename):

    try:                             # Try to open file: EAFP

        f = open(filename, 'rt')

    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find {filename}")

    try:
        reader = csv.reader(f)

        # Dictionary as Counter Design Pattern
        # Create a Default Dictionary to hold count for each state Code
        d = defaultdict(int)

        # Get a new line from File
        first = True
        for row in reader:
            if not first:
                # State is third element
                state = row[2]
    
                # Count this state code: LBYL
                d[state] = 1 + d[state]

            first = False

        f.close()
        return d

    except:
        f.close()
        return {} 


def dictionary_to_list(d):

    # Iterate over the dictionary, build list with [count, state] for each state
    return [ [d[state], state] for state in d ]



# Read in file name from command line
if (len(sys.argv) < 2):
    print("Usage:", sys.argv[0], "<filename>")
else:
    d = read_dict(sys.argv[1])
    res = dictionary_to_list(d)

    # Display the best states: those with lowest count
    res.sort()
    print("States with fewest failures")
    for pair in res[:10]:
        print(pair)

    print()

    # Display the worst states
    res.sort(reverse=True)
    print("States with most failures")
    for pair in res[:10]:
        print(pair)
