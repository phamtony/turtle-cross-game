from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL_BOARD = (-200, 260)
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level_floor = 1
        self.level_update()

    def level_update(self):
        self.clear()
        self.goto(LEVEL_BOARD)
        self.write(f"Level: {self.level_floor}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level_floor += 1
        self.level_update()
