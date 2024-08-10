#Day 12
#Number Guessing Game
import random
from art import logo3

def random_number():
  random_number = random.randint(1,100)
  return random_number
  
def guess_number(random_number, user_guess):
  if user_guess > random_number:
    print("Too high.")
  elif user_guess < random_number:
    print("Too low.")
  else:
    print(f"You got it! The answer was {random_number}")

def difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return 10
  elif difficulty == "hard":
    return 5
  else:
    print("Invalid input.")
    return 0

def game(random_number, user_guess):
  print("Welcome to the Number Guessing Game!")
  print(logo3)
  print("I'm thinking of a number between 1 and 100.")
  random_number = random_number()
  user_guess = 0
  attempts = difficulty()
  while user_guess != random_number and attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    guess_number(random_number, user_guess)
    attempts -= 1
    if attempts == 0:
      print("You've run out of guesses, you lose.")
    elif user_guess != random_number:
      print("Guess again.")
game(random_number, guess_number)
