import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#set up player:
player = Player()
score = Scoreboard()
car_manager = CarManager()




screen.listen()

screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with the car:
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #Detect a successful crossing:
    if player.is_at_finishline():
        player.go_to_start()
        car_manager.increase_speed()
        score.add_points()









    #cars = []
    # if amount_of_cars % 6 == 0:
    #     new_car = CarManager()
    #     cars.append(new_car)
    
    # for car in cars:
    #     car.move_cars()

    # if player.distance(new_car) < 10:
    #         game_is_on = False
    #         score.game_over()
    
    # if player.player_start_position():
    #     score.add_points()
    #     new_car.increase_speed()
    



    # amount_of_cars += 1
    # screen.update()

    # if amount_of_cars  >= 100:
    #     amount_of_cars = 0


    

screen.exitonclick()