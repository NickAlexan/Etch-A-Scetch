from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def fwd():
    pen.forward(10)


def bkwd():
    pen.back(10)


def right():
    pen.right(10)


def left():
    pen.left(10)


screen.listen()
screen.onkey(key="w", fun=fwd)
screen.onkey(key="s", fun=bkwd)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=screen.resetscreen)


screen.exitonclick()