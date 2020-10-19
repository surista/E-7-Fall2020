# Towers of Hanoi
#
# Mike Loukides
# www.oreilly.com/ideas/towers-of-hanoi-every-cs-students-introduction-to-recursion
#
# Jeff Parker
# Added checks for input
#
# $ python hanoi.py
# Usage: hanoi.py <height>
#
# $ python hanoi.py 2
# left   => middle
# left   => right
# middle => right

import sys     # Read command line


def hanoi(height: int, left: str, right: str, middle: str):
    "Move height disks from left to right"
    if (height > 0):
        hanoi(height - 1, left, middle, right)
        print(left, '=>', right)
        hanoi(height - 1, middle, right, left)


if (len(sys.argv) < 2):
    print("Usage:", sys.argv[0], "<height>")
else:
    n = int(sys.argv[1])
    hanoi(n, 'left  ', 'right ', 'middle')
