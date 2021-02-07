from turtle import Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5
STEP_SIZE = 60
MAX_HEIGHT = 250
MIN_HEIGHT = -240


class Paddle(Turtle):
    def __init__(self, x_loc):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT)
        self.speed("fastest")
        self.setheading(90)
        self.goto((x_loc, 0))
        self.bredth = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

    def move_up(self):
        if self.position()[1] < MAX_HEIGHT:
            self.forward(STEP_SIZE)

    def move_down(self):
        if self.position()[1] > MIN_HEIGHT:
            self.back(STEP_SIZE)