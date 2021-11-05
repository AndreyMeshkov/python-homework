import random
from turtle import Turtle
import turtle as t

tim = Turtle()
tim.pensize(1)
tim.speed("fastest")
t.colormode(255)
n = 72


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for i in range(n):
    tim.setheading(360 / n * i)
    tim.circle(100)
    tim.color(random_color())
