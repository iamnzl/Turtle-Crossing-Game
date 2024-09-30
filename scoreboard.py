FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.write("Level : 0", align="center", font= FONT)

    def update_scoreboard(self,level):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level : {level}", align="center", font=FONT)

