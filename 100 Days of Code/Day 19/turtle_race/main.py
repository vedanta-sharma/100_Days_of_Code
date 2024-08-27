
#Day 19
#Etch-a-Sketch app
# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def w():
#   tim.forward(10)

# def a():
#   tim.left(10)

# def s():
#   tim.back(10)

# def d():
#   tim.right(10)

# def c():
#   tim.clear()
#   tim.penup()
#   tim.home()
#   tim.pendown()
  
# screen.onkey(w, "w")
# screen.onkey(a, "a")
# screen.onkey(s, "s")
# screen.onkey(d, "d")
# screen.onkey(c, "c")
# screen.listen()
# screen.exitonclick()


#Turtle Race
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False
for turtle_index in range(0, 6):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[turtle_index])
  new_turtle.penup()
  new_turtle.goto(x=-230, y=y_positions[turtle_index])
  all_turtles.append(new_turtle)

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won! The {winning_color} turtle is the winner!")
      else:
        print(f"You've lost! The {winning_color} turtle is the winner!")
    rand_distance = randint(0, 10)
    turtle.forward(rand_distance)

screen.exitonclick()