from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.x_cord = 0
        self.goto(random.randint(-280, 280), random.randint(-260, 270))

    def move(self, level_floor):
        if level_floor == 1:
            speed = STARTING_MOVE_DISTANCE
        else:
            speed = (level_floor - 1) * MOVE_INCREMENT

        if self.xcor() <= -320:
            self.goto(320, random.randint(-260, 270))

        self.x_cord = self.xcor() - speed
        self.goto(self.x_cord, self.ycor())
