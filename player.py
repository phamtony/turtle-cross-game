from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)

    def move_down(self):
        y_cor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)

    def next_round(self):
        self.goto(STARTING_POSITION)
