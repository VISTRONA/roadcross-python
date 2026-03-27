from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(colors))
        self.penup()
        self.left(180)
        self.goto(270,0)



    def move(self):
        self.forward(10)