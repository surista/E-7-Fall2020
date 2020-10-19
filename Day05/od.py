# od.py
#
# Octal Dump of a file: Mimics the Unix 'od -c' cmmand
# Usage:
#      % python od.py <filename>
#
# Jeff Parker
#
# Bugs:
#     We are handling the special characters one at a time
#     Spacing is not fixed with the odd chararacters

import string
import sys

# Return a string represnting the character
# Most of the strings have length 2: the final set may not
def display(ch):
    # Deal with the whitespace first:
    # printable, but needs special processing
    if (ch == ' '):
        return '  '
    elif (ch == '\t'):
        return '\\t'
    elif (ch == '\n'):
        return '\\n'
    elif (ch == '\r'):
        return '\\r'
    elif ch.isprintable():
        return ch + ' '
    else:
        return str(ord(ch))


# Did the user give me a filename?
if (len(sys.argv) != 2):
    print("Usage: python od.py <filename>")
else:
    # Take the filename
    with open(sys.argv[1], 'r') as f:

        # Read the whole file
        text = f.read()

        while (len(text) > 0):
            # Get the next 16 characters
            line = text[:16]
            text = text[16:]

            # Build a list of the representations
            lst = []
            for ch in line:
                lst.append(display(ch))

            # Paste the elements together and print 
            print(' '.join(lst))

