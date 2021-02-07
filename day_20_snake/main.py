from turtle import Screen, onkey
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()

still_alive = True
while still_alive:
    screen.update()
    onkey(snake.face_up, "Up")
    onkey(snake.face_down, "Down")
    onkey(snake.face_left, "Left")
    onkey(snake.face_right, "Right")
    snake.move()
    scoreboard.display_score()
    time.sleep(snake.speed)

    # detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
        print("nom nom nom")

    # detect collision with wall
    if snake.is_out_of_bounds():
        scoreboard.game_over()
        still_alive = False

    # detect collision with tail
    if snake.is_colliding_with_self():
        scoreboard.game_over()
        still_alive = False

screen.exitonclick()
