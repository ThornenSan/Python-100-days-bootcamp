import turtle as t
import random

tim = t.Turtle()

num_sides = 5

colours = ["red", "blue", "magenta", "green",
           "yellow", "brown", "DeepSkyBlue", "wheat"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)
