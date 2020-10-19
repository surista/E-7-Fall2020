# file.py
#
# Demonstrate the basics of Python file handling
# Usage:
#      % python file.py
#
# Jeff Parker, Summer 2013

my_file = open('script.txt', 'r')
print(my_file)
lines = my_file.readlines()
print(lines)
my_file.close()
