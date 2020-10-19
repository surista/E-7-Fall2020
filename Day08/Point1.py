"""
Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Point(object):
    """Represents a point in 2-D space."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Not implemented yet"

def test():
    one = Point(3, 4)
    print(one)

    two = Point(3, 4)
    print(two)

    print("Are they equal?", one == two)
    
if __name__ == '__main__':
    test()

