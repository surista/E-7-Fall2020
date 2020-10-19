'''
bubble_sort.py

Jeff Parker
Oct 2018
Visualize Bubble Sort
'''

import random
import sys

def initialize_list(size):
    '''Create a list of size random numbers'''
    # Initialize random number generator
    random.seed()

    # Pick a two digit number 
    return [random.randint(10, 99) for i in range(size)]

def sort(lst):
    '''Use Bubble Sort to order a list'''
    debug = True

    swap = True
    count = 0
    while swap:
        swap = False
        if debug:
            print()
            print(count)
            print(lst)
            count = count + 1
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                swap = True
                lst[j], lst[j+1] = lst[j+1], lst[j]
                if debug:
                    print(lst[:j+2])


list_size = 10
if len(sys.argv) > 1:
    list_size = int(sys.argv[1])

unsorted_lst = initialize_list(list_size)
sort(unsorted_lst)
