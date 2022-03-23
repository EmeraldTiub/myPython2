import turtle
t = turtle.Pen()
turtle.bgcolor('black')
t.pencolor('turquoise')
t.speed(0)
t.turtlesize(2, 2, 2)
def up():
    t.forward(50)
def left():
    t.left(90)
def right():
    t.right(90)
def w():
    t.forward(50)
def a():
    t.left(90)
def d():
    t.right(90)
def move(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
turtle.onkeypress(up, "Up")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(w, "w")
turtle.onkeypress(a, "a")
turtle.onkeypress(d, "d")
turtle.listen()
turtle.onscreenclick(move)
