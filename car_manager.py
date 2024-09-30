from turtle import Turtle
import random
#from Demos.SystemParametersInfo import new_x

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)

        self.color(COLORS[random.randint(0,len(COLORS) -1)])
        self.penup()
        random_x = random.randint(150,300)
        random_y = random.randint(-280,275)
        self.goto(random_x,random_y)

    def move(self, level):
        if level == 0:
            new_x = self.xcor() - STARTING_MOVE_DISTANCE
            self.goto(new_x, self.ycor())
        else:
            new_x = self.xcor() - MOVE_INCREMENT*level
            self.goto(new_x, self.ycor())


