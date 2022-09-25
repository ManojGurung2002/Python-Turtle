import turtle
import random

tur = turtle.Turtle()
colors = ['red', 'purple', 'cyan', 'green']
def up():
    tur.setheading(90)
    tur.forward(80)


def down():
    tur.setheading(270)
    tur.forward(80)


def left():
    tur.setheading(180)
    tur.forward(80)


def right():
    tur.setheading(0)
    tur.forward(80)


def clickleft(x, y):
    tur.color(random.choice(colors))


def clickright(x, y):
    tur.circle(30)

    
turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)


turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(right,'Right')
turtle.onkey(left,'Left')

turtle.mainloop()

