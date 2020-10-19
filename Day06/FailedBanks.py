# Failed Banks.py
#
# Read in information from Excel file saved as CSV 
# Usage:
#      % python FailedBanks.py banks.csv
#
# Bank Name,City,ST,CERT,Acquiring Institution,Closing Date,Updated Date
# Fayette County Bank,Saint Elmo,IL,1802,"United Fidelity Bank, fsb",26-May-17,26-Jul-17
#
# Bugs: this treats the first line of the file as valid data

import csv      # Read Comma Separated Values (CSV) files
import sys      # Read filename from command line

# Read in file name from command line
if (len(sys.argv) < 2):
    print("Usage:", sys.argv[0], "<filename>")
else:
    try:                             # Try to open file: EFAP
        f = open(sys.argv[1], 'rt')
    except FileNotFoundError:
        print("No such file", sys.argv[1])
        exit(1) 
        
    try:
        reader = csv.reader(f)

        # Dictionary to hold count for each state Code
        # Dictionary as Counter Design Pattern
        d = { }

        # Get a new line from File
        for row in reader:
            # State is third element 
            state = row[2]

            # Count this state code: LBYL
            if (not state in d):
                d[state] = 1
            else:
                d[state] = 1 + d[state]

        # Iterate over the dictionary and build a list with [count, state]
        res = [[d[state], state] for state in d]
    
        # Display the best states: those with lowest count
        res.sort()
        for pair in res[:10]:
            print(pair)
        
        print()

        # Display the worst states
        res.sort(reverse=True)
        for pair in res[:10]:
            print(pair)
        
    finally:
        f.close()
