from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.shape("turtle")


    def reset_player(self):
        # self.clear()
        self.goto(0, -270)

    def moveUp(self):
        if self.ycor() < 270:
            self.forward(10)


    def moveDown(self):
        if self.ycor() > -270:
            self.backward(10)

    def moveRight(self):
        if self.xcor() < 250:
            self.right(90)
            self.forward(10)
            self.left(90)

    def moveLeft(self):
        if self.xcor() > -250:
            self.left(90)
            self.forward(10)
            self.right(90)

