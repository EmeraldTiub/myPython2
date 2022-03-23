import turtle
t = turtle.Pen()
number = int(turtle.numinput("Number of sides or circles",
             "How many sides or circles in your shape?", 6))
shape = turtle.textinput("Which shape do you want?",
                         "Enter 'p' for polygon or 'r' for rosette:")
t.speed(0)
turtle.Screen().setup(width=0.5, height=0.75, startx=None, starty=None)
for x in range(number):
    if shape == 'r':
        t.circle(100)
        t.circle(90)
    else:
        t.forward (150)
    t.left(360/number)
    t.forward(20)
t.penup()
t.right(90)
t.forward(500)
t.left(90)
t.pendown()
t.pencolor("sky blue")
for x in range(number):
    if shape == 'r':
        t.circle(100)
        t.circle(90)
    else:
        t.forward (150)
    t.left(360/number)
    t.forward(20)


    
t.penup()
t.forward(500)
t.left(90)
t.forward(400)
t.pendown()
t.pencolor("orange")
for x in range(number):
    if shape == 'r':
        t.circle(100)
        t.circle(90)
    else:
        t.forward (150)
    t.left(360/number)
    t.forward(20)

t.penup()
t.left(90)
t.forward(600)
t.pendown()
t.pencolor("green")
for x in range(number):
    if shape == 'r':
        t.circle(100)
        t.circle(90)
    else:
        t.forward (150)
    t.left(360/number)
    t.forward(20)
