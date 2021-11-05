import random
# import turtle
from turtle import Turtle, Screen

tim = Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(10):
#     tim.forward(4)
#     tim.penup()
#     tim.forward(4)
#     tim.pendown()
colors = ["cornflower blue", "chartreuse", "yellow", "firebrick", "purple",
          "medium purple", "black", "green", "blue", "saddle brown", "red"]

# def draw_figure(n):
#     for _ in range(n):
#         tim.forward(100)
#         tim.right(360 / n)
#
#
# for n in range(3, 9):
#     color = random.choice(colors)
#     tim.color(color)
#     draw_figure(n)

tim.pensize(10)
tim.speed(1)

while True:
    color = random.choice(colors)
    tim.color(color)
    tim.forward(20)
    direction = random.randint(0, 3)
    tim.setheading(90 * direction)

# screen = Screen()
# screen.exitonclick()
