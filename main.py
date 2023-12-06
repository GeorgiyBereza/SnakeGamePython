import time
from turtle import Screen, Turtle

from food import Food
from scoreboard import Scoreboard
from snake import Snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Good Old Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with border
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.death()
        screen.update()
        time.sleep(1)
        snake.clear()
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.death()
            screen.update()
            time.sleep(1)
            snake.clear()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()