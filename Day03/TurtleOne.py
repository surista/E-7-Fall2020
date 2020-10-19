# TurtleOne.py
#
# Our first Turtle Program
# Usage:
#      % python TurtleOne.py
#
# Chapter 4 of Downey's Think Python!

import turtle

# Create a Turtle Object
bob: Turtle = turtle.Turtle()

# Print the object
print(bob)

# Draw the edges of a square
for i in range(4):
    bob.fd(100)
    bob.lt(90)

# Wait for the user
turtle.mainloop()
