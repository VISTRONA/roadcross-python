from turtle import Screen
from car_managment import Car
import time

from player import Player

screen = Screen()
screen.setup(width=600 , height=600 )
screen.tracer(0)

car = Car()


player = Player()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")


game = True
while game:
    car.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()