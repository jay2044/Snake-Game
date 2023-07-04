from turtle import Turtle

class Scoreboard(Turtle):
    # Constants
    FONT = ("pixel", 24, "normal")  # Font for the scoreboard
    POSITION = (0, 260)  # Position of the scoreboard on the screen

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(self.POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()  # Clear the scoreboard before updating
        self.write(f"Score: {self.score}", align="center", font=self.FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=self.FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
