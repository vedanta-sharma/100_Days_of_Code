#Day 14
#Higher Lower Game
# from art import logo4, vs
# from game_data import data
# import random
# from replit import clear

# def format_data(account):
#   account_name = account["name"]
#   account_descr = account["description"]
#   account_country = account["country"]
#   return f"{account_name}, a {account_descr}, from {account_country}"
# def check_answer(guess, a_followers, b_followers):
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"
# def game():
#   print(logo4)
#   score = 0
#   game_should_continue = True
#   account_b = random.choice(data)
#   while game_should_continue:
#     account_a = account_b
#     account_b = random.choice(data)
#     while account_a == account_b:
#       account_b = random.choice(data)
#     print(f"Compare A: {format_data(account_a)}")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}")
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)
#     clear()
#     print(logo4)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")
# game()