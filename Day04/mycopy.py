# mycopy.py
#
# Copy file
# Usage:
#      % python mycopy.py original copy
#
# Jeff Parker, September, 2018

import sys


def copy(source: str, dest: str):
    "Copy one file to another"

    # Open the files
    with open(source, 'r') as fin:
        with open(dest, 'w') as fout:

            # Iterate over the input, write to output
            for line in fin:
                fout.write(line)


if (len(sys.argv) == 3):
    copy(sys.argv[1], sys.argv[2])
else:
    print("Usage: mycopy <from> <to>")
