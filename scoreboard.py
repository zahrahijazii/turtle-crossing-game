from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.goto(-210, 260)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level:{self.score}", align="left", font=FONT)
    
    def add_points(self):
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.home()
        self.write("Game Over.", align="center", font=FONT)

