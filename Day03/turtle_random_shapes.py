import turtle

n = 225 # edge length of each square
width = 2  # Pen width
times = 3
s = turtle.getscreen()
s.bgcolor('black')
t = turtle.Turtle()
t.speed(5000)


def circle_shape(t,n,times):
    t.hideturtle()
    t.pensize(width)
    t.pendown()
    for i in range(times):
        t.circle(n)
        t.fd(i+n)
        t.rt(185+i)
        t.fd(n+i)
    t.penup()

def draw_circles(t,n,times):
    for i in range(times):
        t.color("yellow")
        circle_shape(t,n,times)
        t.color("red")
        circle_shape(t,n,times)
        t.color("blue")
        circle_shape(t,n,times)
        t.color("green")
        circle_shape(t,n,times)
        t.color("white")
        circle_shape(t,n,times)
        t.color("orange")
        circle_shape(t,n,times)
        t.color("purple")
        circle_shape(t,n,times)
    # lets user keep screen open until clicked
    s.exitonclick()

draw_circles(t,n,times)

