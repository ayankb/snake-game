from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
from line import Line
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        time.sleep(1)
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            time.sleep(1)
            scoreboard.game_over()


screen.exitonclick()
