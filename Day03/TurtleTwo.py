# TurtleTwo.py
#
# Our second Turtle Program
# Usage:
#      % python TurtleTwo.py
#
# Chapter 4 of Downey's Think Python!

import turtle

# Create a turtle ojbect
bob = turtle.Turtle()

bob.goto(300, 300)

# Draw a picture
for i in range(45):
    # Draw an edge
    bob.fd(200)
    bob.lt(88)

# Hide the Turtle
turtle.ht()

# Wait for the user
turtle.mainloop()
