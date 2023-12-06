from turtle import Turtle
import random

colors = ["blue", "purple", "red", "orange"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # make it in 20n form
        self.color(random.choice(colors))
        self.seth(random.randrange(0,360,45))
        random_x = random.randrange(-280, 280,20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)

