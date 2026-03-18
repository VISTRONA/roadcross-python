from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game = True
while game:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()