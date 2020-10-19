# file3.py
#
# Demonstrate the basics of Python file handling
# Usage:
#      % python file3.py
#
# Jeff Parker, Summer 2013

# Open the file
with open('script.txt', 'r') as my_file:
    # Step through the file
    for line in my_file:
        # print eaach line
        print(line)
