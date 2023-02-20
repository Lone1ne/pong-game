from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()



    def update_scoreboard(self):
        self.write(f"Score: {self.score_p1} - {self.score_p2}", align=ALIGNMENT, font=FONT)

    def increase_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.score_p1 == 5:
            self.goto(0, 0)
            self.write("Player 1 wins the game!", align=ALIGNMENT, font=FONT)
        elif self.score_p2 == 5:
            self.goto(0, 0)
            self.write("Player 2 wins the game!", align=ALIGNMENT, font=FONT)
