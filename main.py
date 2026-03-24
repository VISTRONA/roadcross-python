from turtle import Screen

from player import Player

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Road Crossing Turtle")


player = Player()
player.reset_player()

screen.listen()
screen.onkey(player.moveUp, "Up")
screen.onkey(player.moveDown,"Down")
screen.onkey(player.moveRight,"Right")
screen.onkey(player.moveLeft, "Left")




game_on = True
while game_on:
    screen.update()






screen.exitonclick()