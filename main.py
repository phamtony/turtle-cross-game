import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

CAR_AMOUNT = 15
cars = []
player = Player()
scoreboard = Scoreboard()

for _ in range(CAR_AMOUNT):
    new_car = CarManager()
    cars.append(new_car)

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move(scoreboard.level_floor)

        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() >= FINISH_LINE_Y:
        scoreboard.increase_level()
        player.next_round()

screen.exitonclick()