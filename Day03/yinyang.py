#!/usr/bin/env python3
"""       turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

"""

# Edits added September 2018, JDP

from turtle import *


def yin(radius, color1, color2):
    # Set pen width, color, and fill
    width(3)
    color("black", color1)
    begin_fill()

    # Draw the teardrop and fill it
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()

    # Mode into position for the dot
    left(90)
    up()
    forward(radius*0.35)
    right(90)
    down()

    # Draw the dot in a contrasting color
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()

    # Return to center of the screen
    left(90)
    up()
    backward(radius*0.35)
    down()
    left(90)


def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"


if __name__ == '__main__':
    main()
    turtle.mainloop()
