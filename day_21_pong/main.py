from turtle import Screen, onkey
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
PADDLE_X_LOC = 350

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

right_paddle = Paddle(PADDLE_X_LOC)
left_paddle = Paddle(-PADDLE_X_LOC)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
game_is_on = True
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "i")
screen.onkey(right_paddle.move_down, "k")

while game_is_on:
    screen.update()
    time.sleep(ball.sleep_time)
    ball.progress()
    ball.test_for_wall_bounce(SCREEN_HEIGHT)
    ball.test_for_paddle_bounce(paddle=left_paddle)
    ball.test_for_paddle_bounce(paddle=right_paddle)

    # detect when paddle misses
    if abs(ball.x_pos) > 380:
        if ball.x_pos < 0:
            scoreboard.user2_goal()
        else:
            scoreboard.user1_goal()
        ball.reset_position()
        time.sleep(0.8)

screen.exitonclick()
