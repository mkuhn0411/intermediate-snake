from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("deep pink")
        self.up()
        self.goto(0, 270)
        self.hideturtle()
        self.write_score()

    def write_score(self, game_over = False):
        if game_over:
            self.goto(0, 0)
            self.write("Game Over! Sucks to suck", align=ALIGNMENT, font=FONT)
        else:
            self.clear()
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_to_score(self):
        self.score += 1
        self.write_score()
