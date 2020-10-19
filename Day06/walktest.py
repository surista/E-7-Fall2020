# walk.py
#
# List all files below a point in the file system
#
# Usage:
#    python walk.py <path>
#
# Based on Downey's Think Python, Chapter 14.4

import os
import sys

# Perform a recursive traverse of directories
def walk(dirname):

    # Walk over the files in this directory
    for name in os.listdir(dirname):

        # Construct a full path
        path = os.path.join(dirname, name)

        # print filenames, and traverse directories
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
# Was there anything on the command line?
if len(sys.argv) != 2:
    print("Usage: python walk.py <path>")
else:
    walk(sys.argv[1])
