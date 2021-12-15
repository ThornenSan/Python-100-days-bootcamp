import random
from turtle import Turtle

FOOD_COLOR = ["red", "blue", "magenta", "green",
              "yellow", "brown", "DeepSkyBlue", "wheat"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.food_coloring()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def food_coloring(self):
        random_color = random.choice(FOOD_COLOR)
        self.color(random_color)
