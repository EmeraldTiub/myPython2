import turtle
colors = ['red', 'purple', 'blue', 'green', 'yellow']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor (colors[x%5])
    t.width(x/100+1)
    t.forward(x)
    t.left(60)
