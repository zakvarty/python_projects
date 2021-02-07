from turtle import Turtle

BALL_SIZE = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed("slow")
        self.shapesize(BALL_SIZE)
        self.radius = BALL_SIZE * 10
        self.x_pos = 0
        self.y_pos = 0
        self.x_move = 10
        self.y_move = 10
        self.sleep_time = 0.07

    def progress(self):
        self.x_pos += self.x_move
        self.y_pos += self.y_move
        self.goto(self.x_pos, self.y_pos)

    def test_for_wall_bounce(self, screen_height):
        if abs(self.y_pos) >= screen_height / 2 - self.radius:
            self.y_move *= -1

    def test_for_paddle_bounce(self, paddle):
        is_hitting_right = self.distance(paddle) < 50 and self.x_pos > 320
        is_hitting_left = self.distance(paddle) < 50 and self.x_pos < -320
        if is_hitting_left:
            print("left")
        if is_hitting_right:
            print("right")
        if is_hitting_right or is_hitting_left:
            self.x_move *= -1
            self.sleep_time *= 0.9

    def reset_position(self):
        self.x_pos = 0
        self.y_pos = 0
        self.goto(self.x_pos, self.y_pos)
        self.sleep_time = 0.07
        self.x_move *= -1
