#Day 18
#Turtle Graphics
# from turtle import Turtle, Screen
# import random
# import turtle
# tim = Turtle()
# colors = ["red", "orange", "wheat", "green", "blue", "indigo", "violet", "black"]
# def draw_shape(num_sides):
#   angle = 360 / num_sides
#   for _ in range(num_sides):
#     tim.forward(100)
#     tim.left(angle)

# for shape_side_n in range(3, 11):
#   tim.color(random.choice(colors))
#   draw_shape(shape_side_n)

# screen = Screen()
# screen.exitonclick()

#Random Walk
# tim.pensize(10)
# tim.speed("fast")

# def random_color():
#   r = random.random()
#   g = random.random()
#   b = random.random()
#   random_color = (r, g, b)
#   return random_color

# directions = [0, 90, 180, 270]
# for _ in range(200):
#    tim.pencolor(random_color())
#    tim.forward(50)
#    tim.setheading(random.choice(directions))

#Spirograph
# tim.speed("fastest")
# tim.pensize(2)

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# for _ in range(72):
#   tim.color(random_color())
#   tim.circle(50)
#   tim.left(5)

# turtle.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)

# screen = Screen()
# screen.exitonclick()

# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   rgb_colors.append(new_color)
# print(rgb_colors)

# color_list = [(202, 164, 109), (148, 75, 50), (222, 201, 136), (240, 245, 241), (132, 175, 155), (120, 39, 32), (200, 140, 168), (5, 95, 86), (181, 86, 61), (19, 65, 127), (86, 146, 110), (141, 178, 162), (70, 143, 57), (141, 70, 73), (45, 54, 47), (237, 212, 223), (127, 123, 154), (170, 188, 211), (159, 192, 206), (215, 185, 178), (54, 68, 53), (26, 43, 22), (107, 126, 153), (175, 200, 188), (34, 151, 111), (176, 194, 197), (199, 195, 184), (91, 109, 126)]

# import turtle as t
# import random
# tim = t.Turtle()
# t.colormode(255)
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
# for dot_count in range(1, number_of_dots + 1):
#   tim.dot(20, random.choice(color_list))
#   tim.forward(50)
#   if dot_count % 10 == 0:
#     tim.setheading(90)
#     tim.forward(50)
#     tim.setheading(180)
#     tim.forward(500)
#     tim.setheading(0)
# screen = t.Screen()
# screen.exitonclick()

