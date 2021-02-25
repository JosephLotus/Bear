import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up_turtle, "Up")
screen.onkey(player.down_turtle, "Down")
screen.onkey(player.right_turtle, "Right")
screen.onkey(player.left_turtle, "Left")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect successful crossing
    if player.ycor() > 270:
        scoreboard.player_scores()
        player.reset_pos()
        car_manager.increase_speed()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over_text()
            game_is_on = False

screen.exitonclick()
