"""
Name    : honeycomb.py
Class   : CSCI E-7 (15376)
Author  : S. Urista
HUID    : 81484503
Date    : 9/17/2020
Desc    : Draws six hexagons in honeycomb shape
"""

import turtle


def draw_honeycomb(t, edgeLen, penWidth):
    # repositions turtle to upper left; space for bigger shapes
    s = turtle.getscreen()
    turtle.hideturtle()
    t.pensize(penWidth)
    t.ht()
    t.penup()  # ensures pen is up before moving
    t.lt(180)
    t.fd(250)
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.penup()

    # calls shape drawing function
    for x in range(6):
        honeycomb_shape(t, edgeLen)

    # lets user close screen by clicking on it
    s.exitonclick()


def honeycomb_shape(t, edgeLen):
    # Draws the honeycomb shape
    t.lt(60)
    t.fd(edgeLen)
    t.pendown() # ensure pen is down before drawing
    for i in range(6):
        t.fd(edgeLen)
        t.rt(60)
    t.penup()
    t.rt(60)
    t.fd(edgeLen)
    t.rt(60)


t = turtle.Turtle(visible=False)
t.speed(10)
edgeLen = 200
penWidth = 5

draw_honeycomb(t, edgeLen, penWidth)


