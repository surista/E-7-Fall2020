
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

    buffer = 70-len(s)
    justified = (" ")*buffer+s
    print('0123456789012345678901234567890123456789012345678901234567890123456789')
    return justified




def metathesis(word1: str, word2: str) -> str:
    """
    Takes two strings and swaps the
    first two characters of each string
    """
    swap1 = word1[0:2]
    swap2 = word2[0:2]
    return swap2+word1[2:] + " " + swap1+word2[2:]



def top_edge(columns: int) -> str:
    """
    return string for the top edge, based on number of columns"
    """
    corner = "+"
    unit = "-------+"
    topEdge = corner + (unit*columns)
    return topEdge


def block(col: int, row: int)-> str:
    """
    Parameters
    ----------
    col : columns, int
    row : rows, int
    Returns: string block of n columns and r rows
    -------
    """

    # create top border
    corner = "+"
    unit = "-------+"
    top_border = corner + (unit*col)

    # create rest of block
    left_edge = "|"
    unit = "       |"
    walls = (left_edge + unit*col + "\n")*3
    block = top_border + "\n" + (walls + top_edge(col)+"\n")*row
    return block


print(block(1,1))

print(justify('aaa'))

print(metathesis('doug', 'mike'))