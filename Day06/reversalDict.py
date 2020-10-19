# reversalDict.py 
#
# Look for reversals in a file of words using a dictionary to store words
# Usage:
#      % python reversalDict.py words.txt
#
# Jeff Parker, July, 2018
#
# This version profiles the work

from typing import List, Dict
import sys
import cProfile


def find_reversals(words: Dict[str, None]) -> List[str]:
    "Look for reversals in a Dict"

    # Initialize results
    results = []

    # Look for reversals
    for word in words:
        rev = word[::-1]
        if (word < rev) and (rev in words) and (word not in results):
            results.append(word)

    # Return with results
    return sorted(results)


def read_dict(filename: str) -> Dict[str, None]:
    "Read words from a text file and populate a Dictionary"
    res = {}
    
    try:
        with open(filename, 'r') as words:
            for word in words:
                word = word.lower().strip()
                res[word] = None
            
        return res

    except FileNotFoundError:
        print(f"Could not find file {filename}")
    except:
        print(f"Could not open file {filename}")

    return []


if (len(sys.argv) != 2):
    print("Usage: python reversals <filename>")
else:
    dict = read_dict(sys.argv[1])
    cProfile.run('revs = find_reversals(dict)')

    print(len(revs))

    for word in revs:
        print(word)
