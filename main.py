import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
cars = []
iteration = 0
level = 0
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
stop_game = False
while game_is_on:
    if not stop_game:
        if iteration%10 == 0:
            car = CarManager()
            cars.append(car)
        time.sleep(0.1)
        screen.update()

        #Make the cars move in the cars list
        for i in range(len(cars)):
            cars[i].move(level)

        #Check for all cars in cars list if they have collided with turtle
        for i in range(len(cars)):
            if cars[i].distance(player) <= 20:
                stop_game = True

        #Check if turtle has crossed the road
        won = player.check_win()
        if won:
            level += 1
            scoreboard.update_scoreboard(level)


        iteration += 1
    #Stop the game
    else:
        pass

