import random
# import turtle
# from turtle import Turtle, Screen
# import colorgram

# turtle.colormode(255)
# jugnu = Turtle()
# turtle.colormode(255)
#
# colors = colorgram.extract("61RQCX9SJKL.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)

# color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]

# def rgb_color():
#     color = random.choice(color_list)
#     r = color[0]
#     g = color[1]
#     b = color[2]
#     rand_color = (r, g, b)
#     return rand_color
#

# jugnu.setheading(225)
# jugnu.forward(250)
# jugnu.setheading(0)
#
# def dot_line():
#     for _ in range(10):
#         jugnu.dot(20, random.choice(color_list))
#         jugnu.forward(50)
#
#
# def move():
#     for _ in range(5):
#         dot_line()
#         jugnu.setheading(270)
#         jugnu.forward(50)
#         jugnu.setheading(270)
#         dot_line()
#         jugnu.setheading(90)
#         jugnu.forward(50)
#         jugnu.setheading(90)
#         dot_line()
#
#
# move()

# screen = Screen()
# screen.exitonclick()

"""real solution"""

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()