import turtle
import sys

def edge(t: turtle, edgeLen: int, n: int):
    "Draw the edge of a Koch curve of a given complexity"
    if (n == 1):
        t.fd(edgeLen)
    else:
        edgeLen = edgeLen // 3
        edge(t, edgeLen, n-1)
        t.lt(60)
        edge(t, edgeLen, n-1)
        t.rt(120)
        edge(t, edgeLen, n-1)
        t.lt(60)
        edge(t, edgeLen, n-1)

def snowflake(t: turtle, edgeLen: int, max: int):
    "Draw a Koch Snowflake"
    for i in range(3):
        edge(t, edgeLen, max)
        t.rt(120)


my_turtle = turtle.Turtle()

# Backup to try to center the image

my_turtle.penup()
my_turtle.setpos(-100, 100)
my_turtle.speed(0)
my_turtle.pendown()
max = 5
# Draw the snowflake
snowflake(my_turtle, 270, max)

turtle.mainloop()
