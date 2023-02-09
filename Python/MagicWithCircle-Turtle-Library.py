import turtle #import a turlte library
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("white")
t.pencolor("blue")
t.speed(50)
for i in range(250):
    t.circle(100)
    t.lt(1)
    t.circle(100)
    t.lt(1)
