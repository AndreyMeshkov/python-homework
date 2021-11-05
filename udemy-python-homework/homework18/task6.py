import random
from turtle import Turtle
import turtle as t

tim = Turtle()
tim.pensize(10)
tim.speed(9)
t.colormode(255)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(20)
    tim.setheading(90 * random.randint(0, 3))
