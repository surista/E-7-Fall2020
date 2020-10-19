import turtle

#open screen and set background color
# init turtle and pen size/color
t = turtle.Turtle()
t.color("blue")
t.pensize(4)
t.speed(10)
# draw star shape

for i in range(5):
    t.rt(144)
    t.fd(400)

# with open('sample.txt', 'r') as my_file:
#     for line in my_file:
#         print(line, end="")
#
# with open('words.txt', 'r') as cross_file:
#     for line in cross_file:
#         line = line.strip()
#         if (len(line) == 4) and (line[-1] == 't'):
#             print(line)

# t.goto(300,300)
# for i in range(10):
#     t.circle(50)
#     t.fd(10)

# s.exitonclick()

