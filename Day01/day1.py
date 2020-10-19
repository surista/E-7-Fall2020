
def greeting(name: str) -> str:
    """
    Takes a string and returns a greeting
    """

    return "Hello, "+name+"!"


def justify(s: str) -> str:
    """
    takes a string and returns a string
    padded with leading spaces so last
    letter of input string is column 70
    """

    pad = 70-len(s)
    justified = (" ")*pad+s
    print(justified)
    return justified


def metathesis(word1: str, word2: str) -> str:
    """
    Takes two strings and swaps the
    first two characters of each string
    """
    swap1 = word1[0:2]
    swap2 = word2[0:2]
    swapped = swap2+word1[2:] + " " + swap1+word2[2:]
    return swapped



def top_edge(columns: int) -> str:
    """
    return string for the top edge, based on number of columns"
    """
    corner = "+"
    unit = "---+"
    topEdge = corner + (unit*columns)
    return topEdge


def block(n: int, r: int)-> str:
    """
    Parameters
    ----------
    n : columns, int
    r : rows, int
    Returns: string block of n columns and r rows
    -------
    """

    # create top border
    corner = "+"
    unit = "---+"
    top_border = corner + (unit*n)

    # create rest of block
    left_edge = "|"
    unit = "   |"
    walls = (left_edge + unit*n + "\n")*3
    block = top_border + "\n" + (walls + top_edge(n)+"\n")*r
    return block


# print(block(1,2))
n=3
corner = "+"
unit = "---+"
top_border = corner + (unit * n)
print(top_border)
