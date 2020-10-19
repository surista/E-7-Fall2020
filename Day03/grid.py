"""
Name    : grid.py
Class   : CSCI E-7 (15376)
Author  : S. Urista
HUID    : 81484503
Date    : 9/17/2020
Desc    : Draws an n by x set of boxes based on three parameters:
            a turtle, edge length and number of boxes per side
"""

import turtle


def outer_edge(t, edgeLen, count):
   # repositions turtle to upper left
    t.penup() # ensures pen is up before moving
    t.lt(180)
    t.fd(500)
    t.rt(90)
    t.fd(500)
    t.rt(90)

    # create outer edge of shape
    t.pendown() # ensures pen is down before drawing
    for i in range(4):
        t.fd(edgeLen * count)
        t.rt(90)
    t.penup()


def horizontal_edges(t, edgeLen, count):
    # creates count-1 horizontal inner parallel lines
    for i in range(count - 1):
        t.pendown() # ensures pen is down before drawing
        t.fd(edgeLen)
        t.rt(90)
        t.fd(edgeLen * count)
        t.penup()
        # come back
        t.rt(180)
        t.fd(edgeLen * count)
        t.rt(90)
    t.rt(180)
    t.fd(edgeLen*(count - 1))
    t.lt(90)


def vertical_edges(t, edgeLen, count):
    # creates count-1 vertical inner parallel lines

    for i in range(count - 1):
        t.pendown() # ensures pen is down before drawing
        t.fd(edgeLen)
        t.lt(90)
        t.fd(edgeLen * count)
        t.penup()

        # turtle come back
        t.lt(180)
        t.fd(edgeLen * count)
        t.lt(90)
    t.lt(180)
    t.fd(edgeLen*(count - 1))
    t.rt(90)


def draw_grid(t, edgeLen, count):
    s = turtle.getscreen()
    turtle.ht()  # hides turtle
    t.penup()
    outer_edge(t, edgeLen, count)
    horizontal_edges(t, edgeLen, count)
    vertical_edges(t, edgeLen, count)

    # lets user close screen by clicking on it
    s.exitonclick()


edgeLen = 150
penWidth = 5
count = 5
t = turtle.Turtle(visible=False)
t.pensize(penWidth)
t.speed(10)
draw_grid(t, edgeLen, count)
