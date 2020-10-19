"""
Name    : freestyle.py
Class   : CSCI E-7 (15376)
Author  : S. Urista
HUID    : 81484503
Date    : 9/17/2020
Desc    : Draws repeating, slightly off-setting circles in various colors on black screen
"""

import turtle


def circle_shape(t, n, times):
    # initializes turtle and calls shape drawing fun
    t.pendown()     # ensures pen is down before starting to draw
    for i in range(times):
        t.circle(n)
        t.fd(i + n)
        t.rt(185 + i)
        t.fd(n + i)
    t.penup()


def draw_circles(t, n, times):
    # initializes turtle and calls shape drawing fun
    t.hideturtle()
    t.pensize(width)
    t.pendown()

    for i in range(times):
        t.color("yellow")
        circle_shape(t, n, times)
        t.color("red")
        circle_shape(t, n, times)
        t.color("blue")
        circle_shape(t, n, times)
        t.color("green")
        circle_shape(t, n, times)
        t.color("white")
        circle_shape(t, n, times)
        t.color("orange")
        circle_shape(t, n, times)
        t.color("purple")
        circle_shape(t, n, times)

    # lets user keep screen open until clicked
    s.exitonclick()


t = turtle.Turtle(visible=False)
n = 225         # edge length of each square
width = 1       # Pen width
times = 3       # num of times to repeat circles shape
s = turtle.getscreen()
s.bgcolor('black')
t.speed(100)

draw_circles(t, n, times)

