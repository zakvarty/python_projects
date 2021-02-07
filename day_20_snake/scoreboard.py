from turtle import Turtle

TITLE_FONT = ("Courier", 20, "normal")
TITLE_ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(arg=f"SCORE = {self.score}", align=TITLE_ALIGNMENT, font=TITLE_FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER.", align=TITLE_ALIGNMENT, font=TITLE_FONT)
