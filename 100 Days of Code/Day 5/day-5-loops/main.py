#DAY - 1
#100DaysofCode
# Band Name Generator

# print("Welcome to the Band Name Generator!")
# user_city = input("What's the name of the city you grew up in?\n")
# user_pet = input("What's tne name of your pet?\n")
# print("Your band name could be: " + user_city + " " + user_pet)

#Day 5
#100DaysofCode
# Average Height with loops

# student_heights = input("Input a list of student heights(cm): ").split()
# total_height = 0
# for height in range(0, len(student_heights)):
#   student_heights[height] = int(student_heights[height])
#   total_height += student_heights[height]
# number_of_students = 0
# for n in student_heights:
#   number_of_students += 1
# average_height = round(total_height / number_of_students)
# print("The total height is = ",total_height, "cm")
# print("The number of students is = ",number_of_students)
# print("The average height is = ",average_height, "cm")



#Highest Score
# student_scores = input("Input a list of student scores: ").split()
# i = 0
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#   if student_scores[n] > i:
#     i = student_scores[n]
# print("The highest score in the class is: ", i)



#Adding Even Numbers
# target = int(input("Enter a number between 0 & 1000:"))
# total = 0
# # for i in range(0, target+1):
# #   if i % 2 == 0:
# #     total += i
# for number in range(2, target+1, 2):
#   total += number
# print("The sum of all even numbers between 0 &", target, "is:", total)



#FizzBuzz
# target = int(input("Enter the target number:"))
# for i in range(1, target+1):
#   if i % 3 == 0 and i % 5 == 0:
#     print("FizzBuzz")
#   elif i % 3 == 0:
#     print("Fizz")
#   elif i % 5 == 0:
#     print("Buzz")
#   else:
#     print(i)



#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))
# password_list = []
# for i in range(0, nr_letters):
#   password_list += random.choice(letters)
# for i in range(0, nr_symbols):
#   password_list += random.choice(symbols)
# for i in range(0, nr_numbers):
#   password_list += random.choice(numbers)
# random.shuffle(password_list)
# password = ""
# for i in password_list:
#   password += i
# print(f"Your Password length is: {len(password)}")
# print(f"Your generated password is: {password}")
