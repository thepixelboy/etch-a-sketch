from turtle import Turtle, Screen

leo = Turtle()
screen = Screen()

def move_forwards():
  leo.forward(10)

def move_backwards():
  leo.backward(10)

def move_right():
  leo.right(10)

def move_left():
  leo.left(10)

def clear_screen():
  leo.clear()
  leo.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="Left", fun=move_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="Down", fun=move_backwards)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()