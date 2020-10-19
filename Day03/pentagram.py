"""
Name    : pentagram.py
Class   : CSCI E-7 (15376)
Author  : S. Urista
HUID    : 81484503
Date    : 9/17/2020
Desc    : Draws a pentagram shape; one point pointed straight north; takes three parameters:
            a turtle, edge length and pen width
"""

import turtle

# # init turtle and pen size
# def draw_pentagram(t, edgeLen, penWidth):
#     s = turtle.getscreen()
#     turtle.ht()  # hides turtle
#     t.pensize(penWidth)  # sets line thickness
#
#     # repositions turtle higher up the screen
#     # makes space for larger shapes
#     t.penup()
#     t.ht()
#     t.lt(90)
#     t.fd(300)
#     t.rt(90)
#
#     # get starting angle right based on internal angle of pentagram (36 x 2)
#     t.lt(72)
#
#     # draw penta shape
#     t.pendown()  # ensures pen is down
#     for i in range(5):
#         t.rt(144)
#         t.fd(edgeLen)
#
#     # lets user close screen by clicking on it
#     s.exitonclick()
#

t = turtle.Turtle(visible=False)
t.speed(1)
edgeLen = 50
penWidth = 12
count = 10

# draw_pentagram(t, edgeLen, penWidth)

for i in range(1, count + 1):
    t.pendown()
    t.fd(edgeLen)
    # t.penup()
    t.setpos(edgeLen, edgeLen)

s.exitonclick()