import turtle
colors = ['red','blue','green','orange','purple', 'yellow','pink','magenta','cyan']
pen = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
     pen.pencolor(colors[x%9])
     pen.width(8)
     pen.backward(x)
     pen.left(75)
     pen.pensize(5)
     pen.speed(200)