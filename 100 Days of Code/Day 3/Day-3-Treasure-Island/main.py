#DAY - 3
#100DaysofCode



#BMI Calculator 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi <25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi <30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi <35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")



#Leap Year
# year = int(input("Enter the year: "))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")



#Roller Coaster Bill
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age =int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   elif age >= 45 and age <= 55:
#     print("Everything is going to be ok. Have a free ride on us!")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
#   want_photo = input("Do you want a photo taken? Y or N.")
#   if want_photo == "Y":
#     bill += 3
#   print(f"Your final bill is ${bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride.")



#Python Pizza
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
# if extra_cheese == "Y":
#   bill += 1
# print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")



#Love Calculator
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
# love_score = int(str(true) + str(love))

# if (love_score < 10) or (love_score > 90):
#   print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40 and love_score <= 50):
#   print(f"Your score is {love_score}, you are alright together.")
# else:
#   print(f"Your score is {love_score}.")



#Tresure Island
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n')
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "left" or "right"\n')
#   if choice2 == "left":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You fell into a hole. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")



