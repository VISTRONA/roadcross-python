from turtle import Turtle


move_dist = 10

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.goto(0,-270)
        self.left(90)

    def move_up(self):
        self.forward(move_dist)
    def move_down(self):
        self.forward(-move_dist)
    def move_left(self):
        self.left(90)
        self.forward(move_dist)
        self.right(90)
    def move_right(self):
        self.right(90)
        self.forward(move_dist)
        self.left(90)