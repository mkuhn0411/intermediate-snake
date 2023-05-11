from turtle import Turtle
import random

EDGE = 270

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(0.5, 0.5)
        self.color("purple")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(EDGE * -1, EDGE)
        random_y = random.randint(EDGE * -1, EDGE)
        self.goto(random_x, random_y)
